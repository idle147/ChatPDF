import importlib
from pathlib import Path
from .base import ExtractorBase

_extractor = {}

# 动态导入当前目录下的所有以 _extractor.py 结尾的模块
for file in Path(__file__).parent.iterdir():
    if file.name.endswith("_extractor.py"):
        module_name = file.stem

        # 使用绝对路径导入模块
        module = importlib.import_module(f"{__name__}.{module_name}")
        # 获取模块中的所有以Extractor结尾的类，并实例化
        for name in dir(module):
            if not name.endswith("Extractor"):
                continue
            class_modules = getattr(module, name)
            # 断言声明了 suffix_list 属性
            assert hasattr(class_modules, "suffix_list"), f"Module {module.__name__} Class {name} must have 'suffix_list' attribute."
            # 注册到 _extractor 字典中
            for suffix in set(class_modules.suffix_list):
                assert suffix not in _extractor, f"Suffix {suffix} already registered."
                _extractor[suffix] = class_modules


class Extractor:
    @staticmethod
    def create_extractor(file_path: Path) -> ExtractorBase:
        if not isinstance(file_path, Path):
            file_path = Path(file_path)
        file_suffix = file_path.suffix.lower()
        extractor_class = _extractor.get(file_suffix)
        if extractor_class is None:
            raise ValueError(f"Unsupported file type: {file_suffix}")
        return extractor_class.Extractor(file_path)

    @staticmethod
    def extract_text(file_path: Path):
        extractor = Extractor.create_extractor(file_path)
        return extractor.extract_text()
