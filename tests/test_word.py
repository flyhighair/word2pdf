import pytest

from word2pdf.word import Word


class TestGetName:
    @pytest.mark.parametrize(
        "word, expected_name",
        [
            (Word("tests/mocks/tmp.doc"), "tmp"),
            (Word("tests/mocks/tmp.docx"), "tmp"),
        ],
    )
    def test_拡張子無しのファイル名を返す(self, word, expected_name):
        assert word.get_name() == expected_name
