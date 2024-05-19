import re

from bs4 import BeautifulSoup

from utils import clean_words, get_phrases


class PostsAnalyzer:
    def __init__(self, post: BeautifulSoup):
        self.post: BeautifulSoup = post
        self.words: list[str] = []
        self.text: str = ""
        self.get_text()

    def get_text(self) -> None:
        """Get text paragraphs from BeautifulSoup object."""
        paragraphs = self.post.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        self.words = re.findall(r"\b\w+\b", text)
        self.text = " ".join(self.words)

    def analyze(self) -> dict:
        """Return dict of analyzed posts data."""
        analyzed_data = {
            "words_count": self.get_word_count(),
            "letters_count": self.get_letters_count(),
            "key_phrases": self.get_common_phrases(),
        }
        return analyzed_data

    def get_word_count(self) -> int:
        """Return number of words used in a paragraph."""
        return len(self.words)

    def get_letters_count(self) -> int:
        """Return number of letters used in a paragraph."""
        letters = re.findall(r"[a-zA-Z]", self.text)
        return len(letters)

    def get_common_phrases(self, maximum_length: int = 3) -> list[str]:
        """Return list of most common phrases from the text."""
        words = clean_words(self.text)
        phrases = get_phrases(words, maximum_length)

        phrases_sorted = sorted(phrases.items(), key=lambda x: x[1], reverse=True)[:3]
        return [" ".join(item[0]) for item in phrases_sorted]
