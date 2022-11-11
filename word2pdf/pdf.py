import os
import re

from word2pdf.word import Word


class Pdf:
    """変換後のPDFファイル"""

    def __init__(self, path: str, word: Word) -> None:
        if not self.__is_valid(path):
            raise AttributeError("PDF path is invalid.")

        self.__path = path
        self.__word = word

    def get_path(self) -> str:
        """パスを取得する"""
        return self.__get_dirname() + self.__get_name_with_ext()

    def __get_dirname(self) -> str:
        if not self.__is_pdf_file(self.__path):
            if self.__path[-1] == "/":
                return self.__path

            return self.__path + "/"

        return os.path.dirname(self.__path) + "/"

    def __get_name(self) -> str:
        # PDFファイル名が指定されていなければWordファイルと同名にする
        if not self.__is_pdf_file(self.__path):
            return self.__word.get_name()

        return os.path.splitext(os.path.basename(self.__path))[0]

    def __get_name_with_ext(self) -> str:
        return self.__get_name() + ".pdf"

    @classmethod
    def __is_valid(cls, path: str) -> bool:
        # PDFファイル名が指定されているかチェック
        if not cls.__is_pdf_file(path):
            # 指定されていなければ、存在するディレクトリかチェック
            if not os.path.isdir(path):
                return False

        paths = re.split(r"(?<=\/).+\.pdf$", path)
        # PDFファイルが置かれるディレクトリが存在するかチェック
        if not os.path.isdir(paths[0]):
            return False

        return True

    @staticmethod
    def __is_pdf_file(path: str) -> bool:
        return re.search(r".+\.pdf$", path) is not None
