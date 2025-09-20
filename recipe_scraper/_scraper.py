import json

from bs4 import BeautifulSoup
from recipe_scraper._exceptions import RecipeScraperMethodNotImplemented


class Scraper:
    html: str
    website_url: str
    soup: BeautifulSoup

    def __init__(self, html: str, url: str):
        self.html = html
        self.website_url = url
        self.soup = BeautifulSoup(html, 'html.parser')

    def title(self) -> str:
        """Title of the recipe."""
        raise RecipeScraperMethodNotImplemented("title")

    def description(self) -> str:
        """Description of the recipe."""
        raise RecipeScraperMethodNotImplemented("description")

    def instructions(self) -> list[str]:
        """Instructions on how to execute the recipe."""
        raise RecipeScraperMethodNotImplemented("instructions")

    def print(self) -> dict:
        """Returns a dictionary with the recipe information."""
        data = {
            "title": self.title(),
            "description": self.description(),
            "instructions": self.instructions()
        }

        print(json.dumps(data, indent=2))