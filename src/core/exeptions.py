class RestartScriptException(Exception):
    """
    Custom Exception that instructs to restart the script.
    """
    def __init__(
            self,
            message=(
                "An error occurred. Please restart the script, "
                "it will continue from where it left off."
            )
    ):
        self.message = message
        super().__init__(self.message)
