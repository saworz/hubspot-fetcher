import logging
from datetime import date

import requests
from bs4 import BeautifulSoup

from utils import convert_str_to_date, get_latest_posts


class HubspotFetcher:
    def __init__(self):
        self.base_url = "https://blog.hubspot.com"

    @staticmethod
    def get_scrapped_page(url: str) -> BeautifulSoup | None:
        """Return parsed HTML page content."""
        response = requests.get(url)
        if not response.status_code == 200:
            logging.error(
                f"Failed to retrieve page {url}. Error: {response.status_code}"
            )
            return
        return BeautifulSoup(response.content, "html.parser")

    def scrap_blog_main_page(self) -> dict[str, date] | None:
        """Scrap all posts from blog page and return it as a dict of link:date."""
        soup = self.get_scrapped_page(self.base_url)
        if not soup:
            return

        posts = soup.find_all("div", class_="blog-post-card-body")

        posts_data = {}
        for post in posts:
            post_link = post.find("a")["href"]
            post_date = convert_str_to_date(post.find("time")["datetime"])

            if post_link and post_date:
                posts_data[post_link] = post_date
        return posts_data

    def get_posts(self, amount: int = 3) -> None:
        """Return a list of scraped latest posts."""
        posts_data = self.scrap_blog_main_page()
        if not posts_data:
            logging.error("Error while scraping posts.")
            return

        post_urls = get_latest_posts(posts_data, amount)
        for url in post_urls:
            post = self.get_scrapped_page(url)
            print(post)
