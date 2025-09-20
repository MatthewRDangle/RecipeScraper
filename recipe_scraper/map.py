from .scrapers.mccormick import McCormickScraper
from recipe_scraper._scraper import Scraper

scrapers_map: dict[str, type[Scraper]] = {
    "www.mccormick.com": McCormickScraper
}