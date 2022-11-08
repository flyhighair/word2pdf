import sys

import fire
from docx2pdf import convert


def main(input_file_path: str, output_path: str = './') -> None:
    try:
        convert(input_file_path, output_path)
    except Exception as e:
        raise e
    else:
        print('Output File: %s' % output_path)
        sys.exit(0)


if __name__ == '__main__':
    fire.Fire(main)
