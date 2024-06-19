class MissingSettingError(Exception):
    """Raised when a required setting is missing."""

    def __init__(self, setting: str) -> None:  # noqa: D107
        super().__init__(f"{setting} setting is missing")
