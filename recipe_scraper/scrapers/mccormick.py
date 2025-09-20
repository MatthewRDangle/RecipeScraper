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

    def instructions(self) -> list[str]:
        instructions = []

        int_el = self.soup.find("div", {"class": "ff-body fs-body-60 main-recipe__text rte rte--article"})
        for el in int_el.findAll("li"):
            text = el.get_text()
            if text:
                instructions.append(text)

        return instructions