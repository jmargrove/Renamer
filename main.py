import os
from datetime import datetime
from utils.constants import FILE_ARG_ERROR
from utils.kebab_case import kebab_case
import argparse

from utils.parse_file import parse_file


def renamer():
    # Get the file name
    parser = argparse.ArgumentParser(
        description="Formats file to kebab-case_yyMMdd."
    )
    parser.add_argument("file", type=str, help="The file to operate on.")
    args = None
    try:
        args = parser.parse_args()
    except:
        raise ValueError(FILE_ARG_ERROR)

    full_file_name = args.file

    [wd, file_name, extension] = parse_file(full_file_name)
    new_name = kebab_case(file_name)

    old_name = f'{wd}/{file_name}{extension}'

    # Get the date it was created at
    created_at = os.path.getmtime(old_name)
    date = datetime.utcfromtimestamp(created_at)
    formatted_date = date.strftime('%y%m%d')

    # Rename the file
    new_formatted_name = f'{new_name}_{formatted_date}{extension}'
    new_name = f'{wd}/{new_formatted_name}'
    os.rename(old_name, new_name)

    print(new_name)
    return new_formatted_name


if __name__ == "__main__":
    renamer()
