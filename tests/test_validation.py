from word2pdf.validation import isValidOutputPdfPath, isValidWordFilePath


class TestIsValidWordFilePath:
    def test_正常なパスではTrueを返す(self):
        assert isValidWordFilePath("tests/mocks/tmp.doc")
        assert isValidWordFilePath("tests/mocks/tmp.docx")

    def test_Word以外のファイルパスではFalseを返す(self):
        assert not isValidWordFilePath("tests/mocks/tmp.do")

    def test_存在しないWordファイルパスではFalseを返す(self):
        assert not isValidWordFilePath("tests/mocks/none.doc")


class TestIsValidOutputPdfPath:
    def test_正常なパスではTrueを返す(self):
        assert isValidOutputPdfPath("tests/")
        assert isValidOutputPdfPath("tests/output.pdf")

    def test_存在しないディレクトリパスを含んでいる場合はFalseを返す(self):
        assert not isValidOutputPdfPath("test/")
        assert not isValidOutputPdfPath("test/output.pdf")
