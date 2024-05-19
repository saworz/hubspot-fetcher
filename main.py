import logging
from utils import print_to_console
from fetch_posts import HubspotFetcher

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    fetcher = HubspotFetcher()
    posts_data = fetcher.get_posts()
    print_to_console(posts_data)
