from .base import ExtractorBase
import docx


class DOCXExtractor(ExtractorBase):
    suffix_list = [".docx", ".doc"]

    def extract_text(self):
        document = docx.Document(self.file_path)
        contents = [paragraph.text.strip() for paragraph in document.paragraphs if paragraph.text.strip()]
        return contents
