import argparse
import re
from typing import Sequence


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


# From https://gist.github.com/johnjohndoe/4024222
# Files (not deleted) in the index
# files=$(git diff-index --name-status --cached HEAD | grep -v ^D | cut -c3-)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_hook_value = 0

    for filename in args.filenames:
        return_from_file_fix = hook_check_file(filename)
        if return_from_file_fix:
            print(f"Fixing {filename}")
        return_hook_value = return_hook_value | return_from_file_fix

    return return_hook_value


if __name__ == "__main__":
    raise SystemExit(main())
