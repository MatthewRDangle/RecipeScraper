from typing import List
from bs4 import PageElement, BeautifulSoup
from recipe_scraper._scraper import Scraper

class AllRecipesScraper(Scraper):

    def __init__(self, html: str, url: str):
        super().__init__(html, url)

    def title(self) -> str:
        return self.soup.find("h1").get_text()

    def description(self) -> str:
        desc = ""

        desc_el = self.soup.find("div", {"id": "article-header--recipe_1-0"})
        if desc_el:
            desc = desc_el.find("p").get_text()

        return desc

    def prep_time(self) -> int:
        local_prep_time: int = 0

        info_el: BeautifulSoup | None = self.soup.find("div", {"id": "mm-recipes-details_1-0"})
        if info_el:
            content_el = info_el.find("div", {"class": "mm-recipes-details__content"})
            if content_el:
                info_list: List[PageElement] = info_el.findAll("div", {"class": "mm-recipes-details__item"})
                if info_list and info_list[0]:
                    tmp_prep_time_all_char = info_list[0].text.strip()
                    tmp_prep_time_digit_only = ''.join(char for char in tmp_prep_time_all_char if char.isdigit())
                    local_prep_time = int(tmp_prep_time_digit_only)

        return local_prep_time

    def cook_time(self) -> int:
        local_prep_time: int = 0

        info_el: BeautifulSoup | None = self.soup.find("div", {"id": "mm-recipes-details_1-0"})
        if info_el:
            content_el = info_el.find("div", {"class": "mm-recipes-details__content"})
            if content_el:
                info_list: List[PageElement] = info_el.findAll("div", {"class": "mm-recipes-details__item"})
                if info_list and info_list[1]:
                    tmp_prep_time_all_char = info_list[1].text.strip()
                    tmp_prep_time_digit_only = ''.join(char for char in tmp_prep_time_all_char if char.isdigit())
                    local_prep_time = int(tmp_prep_time_digit_only)

        return local_prep_time

    def instructions(self) -> list[str]:
        instructions = []

        info_el = self.soup.find("ol", {"id": "mntl-sc-block_2-0"})
        if info_el:
            for el in info_el.findAll("li"):
                text = el.text.strip()
                if text:
                    instructions.append(text)

        return instructions

    def ingredients(self) -> list[str]:
        ingredients = []

        info_el = self.soup.find("div", {"id": "mm-recipes-structured-ingredients_1-0"})
        if info_el:
            info_list = info_el.find("ul")
            if info_list:
                for el in info_list.findAll("li"):
                    text = el.text.strip()
                    if text:
                        ingredients.append(text)

        return ingredients