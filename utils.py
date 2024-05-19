import logging
from datetime import date, datetime


def convert_str_to_date(date_string: str) -> date | None:
    """Convert string to date object and return it or log an error if date string is invalid."""
    try:
        return datetime.strptime(date_string, "%m/%d/%y").date()
    except ValueError:
        logging.error("Invalid date format.")


def get_latest_posts(posts: dict, amount: int) -> list[str]:
    """Return a list of link to the latest posts."""
    return [
        item[0]
        for item in sorted(posts.items(), key=lambda x: x[1], reverse=True)[:amount]
    ]
