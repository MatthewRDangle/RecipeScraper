# Recipe Scraper
This project was built for personal needs to easily extract a recipe from a website instead of copying and pasting
the data manually. This project is not intended to be used as a python package nor guaranteed to stay up to date. 
This project is not designed to quickly scrape many recipes across multiple websites. The intended use is to visit a 
website first, and if you like the recipe, to then download the recipe onto your computer.

## Development
Install python `3.13.0` and then run `make init` to install all dependencies.

## Forks
Feel free to fork this project if you wish to develop your own version. You assume all legal responsibility for your 
fork; no warranty or support is provided.

## How to Use
To use this project, follow these steps:
1. Visit a website that contains a recipe you want to scrape.
2. Copy the URL of the recipe page.
3. Execute `python3 -m <path to recipe_scraper directory>` from a terminal.
4. Paste the URL into the terminal and press enter when prompted.
    * Only websites included in the internal scrapers directory are supported.
5. The recipe will load into the terminal once fetched.