import os
import re

from word2pdf.word import Word


class Pdf:
    def __init__(self, path: str, word: Word) -> None:
        if not self.__is_valid(path):
            raise AttributeError("PDF path is invalid.")

        self.__path = path
        self.__word = word

    def get_path(self) -> str:
        return self.__get_dirname() + self.__get_name_with_ext()

    def __get_dirname(self) -> str:
        if not self.__is_pdf_file(self.__path):
            if self.__path[-1] == "/":
                return self.__path

            return self.__path + "/"

        return os.path.dirname(self.__path) + "/"

    def __get_name(self) -> str:
        if not self.__is_pdf_file(self.__path):
            return self.__word.get_name()

        return os.path.splitext(os.path.basename(self.__path))[0]

    def __get_name_with_ext(self) -> str:
        return self.__get_name() + ".pdf"

    @classmethod
    def __is_valid(cls, path: str) -> bool:
        if not cls.__is_pdf_file(path):
            if not os.path.isdir(path):
                return False

        paths = re.split(r"(?<=\/).+\.pdf$", path)
        if not os.path.isdir(paths[0]):
            return False

        return True

    @staticmethod
    def __is_pdf_file(path: str) -> bool:
        return re.search(r".+\.pdf$", path) is not None
