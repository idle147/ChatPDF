from abc import ABC, abstractmethod


class ExtractorBase(ABC):
    suffix_list = []

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def extract_text(self):
        pass
