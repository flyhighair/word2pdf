import fire
from docx2pdf import convert

from word2pdf.pdf import Pdf
from word2pdf.word import Word


def main(input_file_path: str, output_path: str = "./") -> None:
    """WordファイルをPDFファイルに変換する

    Parameters
    ----------
    input_file_path: str
        変換するWordファイルのパス
    output_path: str
        変換したPDFファイルの格納先ディレクトリもしくは任意のファイル名を含んだパス
    """
    word = Word(input_file_path)
    pdf = Pdf(output_path, word)

    try:
        convert(word.path, pdf.get_path())
    except Exception as e:
        raise e
    else:
        print("Output File: %s" % pdf.get_path())


if __name__ == "__main__":
    fire.Fire(main)
