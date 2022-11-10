import pytest

from word2pdf.error import ValidationError
from word2pdf.word2pdf import main


def test_正常終了(mocker):
    mock = mocker.patch("word2pdf.word2pdf.convert")

    main("tests/mocks/tmp.docx")

    mock.assert_called_once_with("tests/mocks/tmp.docx", "./")


def test_入力パスが不正でエラー(mocker):
    mocker.patch("word2pdf.word2pdf.convert")

    with pytest.raises(ValidationError) as e:
        main("./none.do")

    assert str(e.value) == "Input file does not exist."


def test_出力パスが不正でエラー(mocker):
    mocker.patch("word2pdf.word2pdf.convert")

    with pytest.raises(ValidationError) as e:
        main("tests/mocks/tmp.docx", "none/")

    assert str(e.value) == "Output path is invalid."
