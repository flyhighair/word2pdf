# word2pdf

word2pdf is CLI to convert a Microsoft Word file to a Pdf file.

## Requirement

- MacOS
- Microsoft Word
- Python ^3.10
- Poetry

## Installation

```bash
git clone https://github.com/flyhighair/word2pdf.git
cd word2pdf
poetry install
```

## Usage

command

```bash
poetry run python -m word2pdf.word2pdf INPUT_FILE_PATH <flags>
```

help

```bash
NAME
    word2pdf.py

SYNOPSIS
    word2pdf.py INPUT_FILE_PATH <flags>

POSITIONAL ARGUMENTS
    INPUT_FILE_PATH
        Type: str

FLAGS
    --output_path=OUTPUT_PATH
        Type: str
        Default: './'

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```
