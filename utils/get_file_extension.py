import re


def get_file_extension(file_name: str):
    # Remove empty spaces
    empty_string_pattern = re.compile(r'/s+')
    cleaned_file_name = re.sub(empty_string_pattern, '', file_name)

    matched_extension = re.search(r'\..+$', cleaned_file_name)
    if not matched_extension:
        return ''
    extension = matched_extension.group()
    # Remove stop
    cleaned_extension = extension.replace('.', '')

    # Is the extension alpha-numeric
    if not cleaned_extension.isalnum():
        raise NameError(
            'Error: check the file extension, renamer only works with alpha numerics.'
        )

    return cleaned_extension
