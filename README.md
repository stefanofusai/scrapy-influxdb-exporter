# scrapy-influxdb-exporter

Export Scrapy spider stats to InfluxDB.

This package uses [uv](https://docs.astral.sh/uv/) for project management. To get started, ensure that **uv** is installed on your machine and updated to the `0.5.6` version. Detailed installation instructions for **uv** can be found [here](https://docs.astral.sh/uv/getting-started/installation/).

## Installation

```bash
uv add scrapy-influxdb-exporter
```

## Usage

Add the following settings to your Scrapy project settings file:

```python
INFLUXDB_DATABASE = ...
INFLUXDB_HOST = ...
INFLUXDB_MEASUREMENT_NAME = ...
INFLUXDB_ORG = ...
INFLUXDB_TOKEN = ...
STATS_CLASS = "scrapy_influxdb_exporter.InfluxDBStatsCollector"
```

## Development

```bash
uv sync --frozen --group=development
uv run --frozen pre-commit install --install-hooks
uv run --frozen pre-commit install --hook-type=commit-msg
```

## Acknowledgments

This project was inspired by [scrapy-prometheus-exporter](https://github.com/rangertaha/scrapy-prometheus-exporter) by [@rangertaha](https://github.com/rangertaha) and [this article](https://mikulskibartosz.name/how-to-monitor-scrapy-spiders-using-influxdb-and-grafana) by [@mikulskibartosz](https://github.com/mikulskibartosz).

## Contributing

Contributions are welcome! To get started, please refer to our [contribution guidelines](https://github.com/stefanofusai/scrapy-influxdb-exporter/blob/main/CONTRIBUTING.md).

## Issues

If you encounter any problems while using this package, please open a new issue [here](https://github.com/stefanofusai/scrapy-influxdb-exporter/issues).
