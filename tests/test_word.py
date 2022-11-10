from word2pdf.word import Word


class TestGetName:
    def test_拡張子無しのファイル名を返す(self):
        word1 = Word("tests/mocks/tmp.doc")
        word2 = Word("tests/mocks/tmp.docx")

        assert word1.get_name() == "tmp"
        assert word2.get_name() == "tmp"
