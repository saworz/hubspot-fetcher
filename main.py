import logging

from fetch_posts import HubspotFetcher

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    fetcher = HubspotFetcher()
    fetcher.get_posts()
