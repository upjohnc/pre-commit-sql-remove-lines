from precommit_sql_clean import remove_endlines


def test_my_fakefs_test(fs):
    # "fs" is the reference to the fake file system
    file_name = "/var/data/xx1.txt"
    file_content = "select *"
    fs.create_file(file_name, contents=file_content)
    _ = remove_endlines(file_name)
    with open(file_name) as f:
        result = f.read()

    assert file_content == result


def test_basic_file_with_extra_lines(fs):
    # "fs" is the reference to the fake file system
    file_name = "/var/data/xx1.txt"
    file_content_base = "select *"
    file_content = f"{file_content_base}\n  \n"
    fs.create_file(file_name, contents=file_content)
    _ = remove_endlines(file_name)
    with open(file_name) as f:
        result = f.read()

    assert file_content_base == result


def test_empty_file_with_extra_lines(fs):
    # "fs" is the reference to the fake file system
    file_name = "/var/data/xx1.txt"
    file_content = ""
    fs.create_file(file_name, contents=file_content)
    _ = remove_endlines(file_name)
    with open(file_name) as f:
        result = f.read()

    assert file_content == result


def test_blank_lines_file_with_extra_lines(fs):
    # "fs" is the reference to the fake file system
    file_name = "/var/data/xx1.txt"
    file_content = "    "
    fs.create_file(file_name, contents=file_content)
    _ = remove_endlines(file_name)
    with open(file_name) as f:
        result = f.read()

    assert "" == result


# empty file
# basic file


# use
