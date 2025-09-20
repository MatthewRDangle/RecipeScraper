from _version import __version__

class RecipeScraperMethodNotImplemented(NotImplementedError):
    """A required scraper method was not implemented."""

    def __init__(self, method: str):
        message = f"Method {method} was not implemented but is required by the scraper class."
        super().__init__(message)

class RecipeScrapperException(Exception):
    """Base class for RecipeScraper exceptions."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"RecipeScraper v{__version__}: {self.message}"