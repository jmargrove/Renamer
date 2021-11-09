import sys
import os
from datetime import datetime
import re
from utils.get_file_extension import get_file_extension
from utils.kebab_case import kebab_case


def renamer():
    # Get the file name
    full_file_name = sys.argv[1]

    extension = get_file_extension(full_file_name)
    file_name = re.sub(r'\..+$', '', full_file_name)
    new_name = kebab_case(file_name)

    file_name = re.sub(r'\..+$', '', full_file_name)
    wd = os.getcwd()
    old_name = f'{wd}/{file_name}.{extension}'

    # Get the date it was created at
    created_at = os.path.getmtime(old_name)
    date = datetime.utcfromtimestamp(created_at)
    formatted_date = date.strftime('%y%m%d')

    # Rename the file
    new_formatted_name = f'{new_name}_{formatted_date}.{extension}'
    new_name = f'{wd}/{new_formatted_name}'
    os.rename(old_name, new_name)

    print(f'🚀 Renamed the file {full_file_name} to {new_formatted_name}')


if __name__ == "__main__":
    renamer()
