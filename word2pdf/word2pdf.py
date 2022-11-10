import fire
from docx2pdf import convert

from word2pdf.error import ValidationError
from word2pdf.validation import isValidOutputPdfPath, isValidWordFilePath


def main(input_file_path: str, output_path: str = "./") -> None:
    if not isValidWordFilePath(input_file_path):
        raise ValidationError("Input file does not exist.")

    if not isValidOutputPdfPath(output_path):
        raise ValidationError("Output path is invalid.")

    try:
        convert(input_file_path, output_path)
    except Exception as e:
        raise e
    else:
        print("Output File: %s" % output_path)


if __name__ == "__main__":
    fire.Fire(main)
