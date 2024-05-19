import logging
import re
from datetime import date, datetime

from consts import STOP_WORDS


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


def clean_words(text: str) -> list[str]:
    """Return list of words without stopwords and special characters."""
    text = re.sub(r"[.!?,:;/\-\s]", " ", text)
    text = re.sub(r"[\\|@#$&~%\(\)*\"]", "", text)

    words = text.split(" ")
    return [w for w in words if len(w) and w.lower() not in STOP_WORDS]


def get_phrases(
    words: list[str], maximum_length: int, minimum_repeat: int = 2
) -> dict[tuple[str, ...], int]:
    """Return dict of phrases from the text."""
    phrases = {}
    size = maximum_length
    while size > 0:
        pos = 0
        while pos + size <= len(words):
            phrase = words[pos: pos + size]
            phrase = tuple(w.lower() for w in phrase)
            if phrase in phrases:
                phrases[phrase] += 1
            else:
                phrases[phrase] = 1
            pos += 1
        size -= 1

    return {k: v for k, v in phrases.items() if v >= minimum_repeat}


def print_to_console(posts_data: dict) -> None:
    """Print the data to the console."""
    for url, data in posts_data.items():
        logging.info("Fetched and analyzed data for:")
        logging.info(f"url: {url}")
        for key, value in data.items():
            logging.info(f"{key}: {value}")
