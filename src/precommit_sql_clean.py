import re


def remove_endlines(file_content: str) -> str:

    file_lines = file_content.splitlines()

    if len(file_lines) < 1:
        return file_content

    while re.search(r"^\s*$", file_lines[-1]) is not None:
        if len(file_lines) == 1:
            file_lines = re.sub(r"\s*$", "", file_lines[0])
            break

        file_lines = file_lines[:-1]
    return "\n".join(file_lines)


def hook_check_file(file_name: str) -> int:
    with open(file_name) as f:
        file_content = f.read()

    check_endlines = remove_endlines(file_content)

    if file_content == check_endlines:
        return 1

    with open(file_name, "w") as f:
        f.write(check_endlines)

    return 0
