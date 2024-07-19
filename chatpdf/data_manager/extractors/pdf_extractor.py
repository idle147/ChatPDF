from .base import ExtractorBase
import PyPDF2


class PDFExtractor(ExtractorBase):
    suffix_list = [".pdf"]

    def extract_text(self):
        contents = []
        with open(self.file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in pdf_reader.pages:
                page_text = page.extract_text().strip()
                raw_text = [text.strip() for text in page_text.splitlines() if text.strip()]
                new_text = ""
                for text in raw_text:
                    new_text += text
                    if text[-1] in [
                        ".",
                        "!",
                        "?",
                        "。",
                        "！",
                        "？",
                        "…",
                        ";",
                        "；",
                        ":",
                        "：",
                        "”",
                        "’",
                        "）",
                        "】",
                        "》",
                        "」",
                        "』",
                        "〕",
                        "〉",
                        "》",
                        "〗",
                        "〞",
                        "〟",
                        "»",
                        '"',
                        "'",
                        ")",
                        "]",
                        "}",
                    ]:
                        contents.append(new_text)
                        new_text = ""
                if new_text:
                    contents.append(new_text)
        return contents
