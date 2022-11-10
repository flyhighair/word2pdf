import os
import re


class Word:
    def __init__(self, file_path: str) -> None:
        if not self.__is_valid(file_path):
            raise AttributeError("Word file is invalid.")

        self.path = file_path

    def get_name(self) -> str:
        return os.path.splitext(os.path.basename(self.path))[0]

    @staticmethod
    def __is_valid(path: str) -> bool:
        return re.search(r".+\.docx?$", path) is not None and os.path.isfile(
            path
        )
