class ApiKeyNotFoundError(Exception):
    """Raised when the OPENAI_API_KEY is not found in the environment."""

    def __str__(self):
        return self.__doc__
