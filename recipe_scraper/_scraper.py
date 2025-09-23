import json

from typing import Union
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

    def prep_time(self) -> int:
        """Preparation time in minutes."""
        raise RecipeScraperMethodNotImplemented("prep_time")

    def cook_time(self) -> int:
        """Cooking time in minutes."""
        raise RecipeScraperMethodNotImplemented("cook_time")

    def instructions(self) -> list[str]:
        """Instructions on how to execute the recipe."""
        raise RecipeScraperMethodNotImplemented("instructions")

    def ingredients(self) -> list[str]:
        """Ingredients used in the recipe."""
        raise RecipeScraperMethodNotImplemented("ingredients")

    def to_json(self) -> dict[str, Union[str, list[str]]]:
        """Returns a JSON representation of the recipe."""
        return {
            "title": self.title(),
            "description": self.description(),
            "prep_time": self.prep_time(),
            "cook_time": self.cook_time(),
            "instructions": self.instructions(),
            "ingredients": self.ingredients(),
        }

    def print(self) -> None:
        """Prints the recipe in JSON format."""

        print(json.dumps(self.to_json(), indent=2))