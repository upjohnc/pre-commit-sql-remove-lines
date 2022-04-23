import re


def remove_endlines(file_content: str) -> str:
    # with open(file_name) as f:
    #     file_thing = f.read()

    file_lines = file_content.splitlines()

    if len(file_lines) < 1:
        return file_content

    while re.search(r"^\s*$", file_lines[-1]) is not None:
        if len(file_lines) == 1:
            file_lines = re.sub(r"\s*$", "", file_lines[0])
            break

        file_lines = file_lines[:-1]
    return "\n".join(file_lines)


if __name__ == "__main__":
    file_name = "./zz_notes/what.sql"
    _ = remove_endlines(file_name=file_name)
# .fs.create_file(file_path, contents = 'test')
# def my_fakefs_test(fs):
#     # "fs" is the reference to the fake file system
#         fs.create_file('/var/data/xx1.txt')
#             assert os.path.exists('/var/data/xx1.txt')
#             pytest
#             plugin: pyfakefs
#             pip install pyfakefs
#
