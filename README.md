# scrapy-influxdb-exporter
A simple package to export Scrapy spider stats to InfluxDB.

## Installation
```bash
pip install scrapy-influxdb-exporter
```

## Usage
Add the following settings to your Scrapy project settings file:
```python
INFLUXDB_DATABASE = ...
INFLUXDB_HOST = ...
INFLUXDB_ORG = ...
INFLUXDB_TOKEN = ...
STATS_CLASS = "scrapy_influxdb_exporter.statscollectors.InfluxDBStatsCollector"
```

## Acknowledgments
This project was inspired by [scrapy-prometheus-exporter](https://github.com/rangertaha/scrapy-prometheus-exporter) and [this article](https://mikulskibartosz.name/how-to-monitor-scrapy-spiders-using-influxdb-and-grafana) by Bartosz Mikulski.

## Contributing
Contributions are welcome! To get started, please refer to our [contribution guidelines](https://github.com/stefanofusai/scrapy-influxdb-exporter/blob/main/CONTRIBUTING.md).

## Issues
If you encounter any problems while using this package, please open a new issue [here](https://github.com/stefanofusai/scrapy-influxdb-exporter/issues).