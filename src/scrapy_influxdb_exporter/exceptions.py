class SettingMissingError(Exception):
    """Raised when a required setting is missing."""

    def __init__(self, setting: str) -> None:
        super().__init__(f"{setting} setting is missing")
