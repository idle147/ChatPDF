
import markdown
from bs4 import BeautifulSoup
from .base import ExtractorBase


class MarkdownExtractor(ExtractorBase):
    suffix_list = [".md"]

    def extract_text(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()
        html = markdown.markdown(markdown_text)
        soup = BeautifulSoup(html, "html.parser")
        contents = [text.strip() for text in soup.get_text().splitlines() if text.strip()]
        return contents
