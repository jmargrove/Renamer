from pathlib import Path
import os


def parse_file(file_path: str):

    relative = Path(file_path)
    absolute = relative.absolute()
    filename = os.path.basename(absolute)
    splitted = os.path.splitext(filename)
    dirname = os.path.dirname(absolute)

    return [dirname, splitted[0], splitted[1]]
