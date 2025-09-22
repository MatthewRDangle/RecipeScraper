import urllib
import requests

from typing import Tuple, Union, Callable
from urllib.parse import SplitResult
from requests import Response
from tldextract import ExtractResult, tldextract
from recipe_scraper._exceptions import InvalidScraperURL
from recipe_scraper._scraper import Scraper


def verify_url(url: str) -> Tuple[str, str]:
    """Verifies the integrity of the URL. If possible, spits back a valid URL string."""

    split_url: SplitResult = urllib.parse.urlsplit(url)
    extracted: ExtractResult = tldextract.extract(split_url.netloc)
    if not extracted.suffix:
        split_url.netloc = f"www.{split_url.netloc}"
    if not extracted.domain:
        raise InvalidScraperURL("Domain not found in URL.")
    if not extracted.suffix:
        raise InvalidScraperURL("Suffix not found in URL.")

    verified_url: str = urllib.parse.urlunsplit(split_url)
    extracted_url: str = f"{extracted.subdomain}.{extracted.domain}.{extracted.suffix}"
    return verified_url, extracted_url

def scrape(url: str, scraper: type[Scraper], err_func: Callable) -> None:
    """Attempt to scrape the website."""

    response: Union[Response, None] = None
    err: bool = False
    try:
        response = requests.get(url, timeout=1)
        response.raise_for_status()
    except requests.exceptions.HTTPError as httperr:
        print("HTTP Error", httperr.args[0])
        err = True
    except requests.exceptions.ReadTimeout as errrt:
        print("Request timed out.")
        err = True
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")
        err = True
    except requests.exceptions.MissingSchema as errmiss:
        print("please include http or https.")
        err = True
    finally:
        if err:
            return err_func()
        else:
            html: str = response.text
            scraper: Scraper = scraper(html, url)
            scraper.print()