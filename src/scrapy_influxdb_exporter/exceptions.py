class SettingMissingError(Exception):
    """Raised when a required setting is missing."""

    def __init__(self, setting: str) -> None:
        """Construct an instance of the SettingMissingError class.

        :param setting: The name of the missing setting.
        :type setting: str
        """
        super().__init__(f"{setting} setting is missing")
