from word2pdf.pdf import Pdf
from word2pdf.word import Word


class TestGetPath:
    def test_ファイルパスを取得する(self):
        word1 = Word("tests/mocks/tmp.doc")
        pdf1 = Pdf("tests/mocks/output.pdf", word1)
        word2 = Word("tests/mocks/tmp.docx")
        pdf2 = Pdf("tests/mocks", word2)
        word3 = Word("tests/mocks/tmp.docx")
        pdf3 = Pdf("tests/mocks/", word3)

        assert pdf1.get_path() == "tests/mocks/output.pdf"
        assert pdf2.get_path() == "tests/mocks/tmp.pdf"
        assert pdf3.get_path() == "tests/mocks/tmp.pdf"
