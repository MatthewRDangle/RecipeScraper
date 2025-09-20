import requests

from recipe_scraper.map import scrapers_map
from recipe_scraper._scraper import Scraper
from tldextract import tldextract, ExtractResult

url: str = "https://www.mccormick.com/blogs/recipes/easy-peach-cobbler?&msclkid=9548525189b311f41c493a9faf2c00a3&utm_source=bing&utm_medium=cpc&utm_campaign=MC_BRD_US-EN_BING_SEM_Summer_NB_REC_MUL_new&utm_term=easy%20peach%20cobbler%20recipe&utm_content=Rec_AllMatch_Easy%20Peach%20Cobbler&gclid=9548525189b311f41c493a9faf2c00a3&gclsrc=3p.ds&gad_source=7&gad_campaignid=22795771325"

extracted: ExtractResult = tldextract.extract(url)
domain: str = f"{extracted.subdomain}.{extracted.domain}.{extracted.suffix}"
scraper: type[Scraper] = scrapers_map[domain]

response = requests.get(url)
html: str = response.text
if html:
    scraper: Scraper = scraper(html, url)
    scraper.print()
else:
    print("Website not supported.")