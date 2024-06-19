from datetime import datetime

from influxdb_client_3 import InfluxDBClient3, Point
from scrapy import Spider
from scrapy.crawler import Crawler
from scrapy.statscollectors import StatsCollector, StatsT

from .exceptions import MissingSettingError


class InfluxDBStatsCollector(StatsCollector):
    """A scrapy stats collector that persists stats to InfluxDB.

    :param StatsCollector: The base class for stats collectors.
    :type StatsCollector: class
    """

    def __init__(self, crawler: Crawler) -> None:
        """Construct an instance of the InfluxDBStatsCollector class.

        :param crawler: The crawler instance.
        :type crawler: Crawler
        """
        super().__init__(crawler)

        self.crawler = crawler
        self.influxdb_host = self._get_setting("INFLUXDB_HOST")
        self.influxdb_org = self._get_setting("INFLUXDB_ORG")
        self.influxdb_database = self._get_setting("INFLUXDB_DATABASE")
        self.influxdb_token = self._get_setting("INFLUXDB_TOKEN")
        self.influxdb_measurement_name = self._get_setting("INFLUXDB_MEASUREMENT_NAME")

        self._init_client()

    def _get_setting(self, name: str) -> str:
        """Get a setting from the crawler settings.

        :param name: The name of the setting.
        :type name: str
        :raises MissingSettingError: If the setting is missing.
        :return: The value of the setting.
        :rtype: str
        """
        setting = self.crawler.settings.get(name)

        if setting is None:
            raise MissingSettingError(name)

        return setting

    def _init_client(self) -> None:
        """Initialize the InfluxDB client."""
        self.client = InfluxDBClient3(
            host=self.influxdb_host,
            org=self.influxdb_org,
            database=self.influxdb_database,
            token=self.influxdb_token,
        )

    def _persist_stats(self, stats: StatsT, spider: Spider) -> None:
        """Persist the spider stats to InfluxDB.

        :param stats: The spider stats.
        :type stats: StatsT
        :param spider: The spider instance to which the stats belong.
        :type spider: Spider
        """
        point = Point(self.influxdb_measurement_name).tag("spider_name", spider.name)

        for key, value in stats.items():
            if isinstance(value, datetime):
                value = value.timestamp()  # noqa: PLW2901

            point = point.field(key, value)

        self.client.write(point)
