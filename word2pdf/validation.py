import os
import re


def isValidWordFilePath(path: str) -> bool:
    if re.search(r".+\.docx?$", path) is None or not os.path.isfile(path):
        return False

    return True


def isValidOutputPdfPath(path: str) -> bool:
    if re.search(r".+\.pdf$", path) is None:
        if not os.path.isdir(path):
            return False

    paths = re.split(r"(?<=\/).+\.pdf$", path)
    if not os.path.isdir(paths[0]):
        return False

    return True
