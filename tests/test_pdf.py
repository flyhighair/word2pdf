import pytest

from word2pdf.pdf import Pdf
from word2pdf.word import Word


class TestGetPath:
    @pytest.mark.parametrize(
        "word, pdf_output_path, expected_path",
        [
            (
                Word("tests/mocks/tmp.doc"),
                "tests/mocks/output.pdf",
                "tests/mocks/output.pdf",
            ),
            (
                Word("tests/mocks/tmp.docx"),
                "tests/mocks",
                "tests/mocks/tmp.pdf",
            ),
            (
                Word("tests/mocks/tmp.docx"),
                "tests/mocks/",
                "tests/mocks/tmp.pdf",
            ),
        ],
    )
    def test_ファイルパスを取得する(self, word, pdf_output_path, expected_path):
        pdf = Pdf(pdf_output_path, word)

        assert pdf.get_path() == expected_path
