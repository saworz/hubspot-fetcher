import re

from bs4 import BeautifulSoup


class PostsAnalyzer:
    def __init__(self, post: BeautifulSoup):
        self.post = post
        self.text = ""
        self.get_text()

    def get_text(self) -> None:
        """Get text paragraphs from BeautifulSoup object."""
        paragraphs = self.post.find_all("p")
        self.text = " ".join([p.get_text() for p in paragraphs])

    def analyze(self) -> dict:
        """Return dict of analyzed posts data."""
        analyzed_data = {}
        analyzed_data["words_count"] = self.get_word_count()
        analyzed_data["letters_count"] = self.get_letters_count()
        return analyzed_data

    def get_word_count(self) -> int:
        """Return number of words used in a paragraph."""
        words = re.findall(r"\b\w+\b", self.text)
        return len(words)

    def get_letters_count(self) -> int:
        """Return number of letters used in a paragraph."""
        letters = re.findall(r"[a-zA-Z]", self.text)
        return len(letters)
