from .base import ExtractorBase


class TXTExtractor(ExtractorBase):
    suffix_list = [".txt"]

    def extract_text(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            contents = [text.strip() for text in f.readlines() if text.strip()]
        return contents
