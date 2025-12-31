from recipe_scraper._exceptions import InvalidScraperURL
from recipe_scraper.helpers import verify_url, scrape
from recipe_scraper.map import scrapers_map
from recipe_scraper._scraper import Scraper


def main() -> None:
    prompt()

def prompt() -> None:
    """Prompt the user for a website URL to scrape."""

    print("Enter the URL of the website you want to scrape:")
    url: str = input()
    if not url:
        return prompt()
    if not url.startswith("https://"):
        url = f"https://{url}"

    # Extract the domain name from the URL.
    domain_url: str = ""
    verified_url: str = ""
    try:
        [verified_url, domain_url] = verify_url(url)
    except InvalidScraperURL:
        print("Invalid URL.")
        prompt()

    # Check if the domain is supported.
    if not domain_url in scrapers_map:
        print("Website not supported.")
        return prompt()
    else:
        scraper: type[Scraper] = scrapers_map[domain_url]
        print(f"Requesting data from {domain_url}")
        scrape(verified_url, scraper, prompt)
        return prompt_request()

def prompt_request() -> None:
    """Asks the user for a website URL to scrape."""

    print("Download another recipe? Y/n:")
    user_input: str = input()
    if user_input.lower() == "y":
        prompt()
    else:
        exit()

if __name__ == "__main__":
    main()