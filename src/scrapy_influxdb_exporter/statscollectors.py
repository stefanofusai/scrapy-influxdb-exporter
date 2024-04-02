from datetime import datetime

from influxdb_client_3 import InfluxDBClient3, Point
from scrapy import Spider
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.statscollectors import StatsCollector, StatsT

from .exceptions import SettingMissingError


class InfluxDBStatsCollector(StatsCollector):
    def __init__(self, crawler: Crawler) -> None:
        super().__init__(crawler)

        self._init_client(crawler.settings)

    def _init_client(self, settings: Settings) -> None:
        influxdb_database = settings.get("INFLUXDB_DATABASE")

        if influxdb_database is None:
            raise SettingMissingError("INFLUXDB_DATABASE")

        influxdb_host = settings.get("INFLUXDB_HOST")

        if influxdb_host is None:
            raise SettingMissingError("INFLUXDB_HOST")

        influxdb_org = settings.get("INFLUXDB_ORG")

        if influxdb_org is None:
            raise SettingMissingError("INFLUXDB_ORG")

        influxdb_token = settings.get("INFLUXDB_TOKEN")

        if influxdb_token is None:
            raise SettingMissingError("INFLUXDB_TOKEN")

        self.client = InfluxDBClient3(
            host=influxdb_host,
            org=influxdb_org,
            database=influxdb_database,
            token=influxdb_token,
        )

    def _persist_stats(self, stats: StatsT, spider: Spider) -> None:
        point = Point("spider_stats").tag("spider_name", spider.name)

        for key, value in stats.items():
            if isinstance(value, datetime):
                value = value.timestamp()  # noqa: PLW2901

            point = point.field(key, value)

        self.client.write(point)
