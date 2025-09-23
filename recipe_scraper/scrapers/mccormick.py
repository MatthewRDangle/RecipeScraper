from typing import List
from bs4 import PageElement, BeautifulSoup
from recipe_scraper._scraper import Scraper

class McCormickScraper(Scraper):

    def __init__(self, html: str, url: str):
        super().__init__(html, url)

    @classmethod
    def website_name(cls) -> str:
        return "www.mccormick.com"

    def title(self) -> str:
        return self.soup.find("h1").get_text()

    def description(self) -> str:
        desc = ""

        desc_el = self.soup.find("div", {"class": "ff-body fs-body-60 main-recipe__excerpt main-recipe__excerpt--desktop"})
        if desc_el:
            desc = desc_el.find("p").get_text()

        return desc

    def prep_time(self) -> int:
        local_prep_time: int = 0

        info_el: BeautifulSoup | None = self.soup.find("ul", {"class": "recipe-info__list"})
        if info_el:
            info_li: List[PageElement] = info_el.findAll("li")
            if info_li and info_li[0]:
                tmp_prep_time_all_char = info_li[0].text.strip()
                tmp_prep_time_digit_only = ''.join(char for char in tmp_prep_time_all_char if char.isdigit())
                local_prep_time = int(tmp_prep_time_digit_only)

        return local_prep_time

    def cook_time(self) -> int:
        local_cook_time: int = 0

        info_el: BeautifulSoup | None = self.soup.find("ul", {"class": "recipe-info__list"})
        if info_el:
            info_li: List[PageElement] = info_el.findAll("li")
            if info_li and info_li[1]:
                tmp_cook_time_all_char = info_li[1].text.strip()
                tmp_cook_time_digit_only = ''.join(char for char in tmp_cook_time_all_char if char.isdigit())
                local_cook_time = int(tmp_cook_time_digit_only)

        return local_cook_time

    def instructions(self) -> list[str]:
        instructions = []

        int_el = self.soup.find("div", {"class": "ff-body fs-body-60 main-recipe__text rte rte--article"})
        for el in int_el.findAll("li"):
            text = el.text.strip()
            if text:
                instructions.append(text)

        return instructions

    def ingredients(self) -> list[str]:
        ingredients = []

        ing_el = self.soup.find("ul", {"class": "recipe-ingredients__list"})
        if ing_el:
            for el in ing_el.findAll("li"):
                text = el.text.strip()
                if text:
                    ingredients.append(text)

        return ingredients