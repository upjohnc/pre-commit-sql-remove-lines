from precommit_sql_clean import remove_endlines


def test_basic_file_no_extra_lines(fs):
    # "fs" is the reference to the fake file system
    # file_name = "/var/data/xx1.txt"
    file_content = "select *"
    # fs.create_file(file_name, contents=file_content)
    result = remove_endlines(file_content)
    # with open(file_name) as f:
    #     result = f.read()

    assert file_content == result


def test_basic_file_with_extra_lines(fs):
    file_content_base = "select *"
    file_content = f"{file_content_base}\n  \n"
    result = remove_endlines(file_content)

    assert file_content_base == result


def test_empty_file_with_extra_lines(fs):
    file_content = ""
    result = remove_endlines(file_content)
    assert file_content == result


def test_blank_lines_file_with_extra_lines(fs):
    file_content = "    "
    result = remove_endlines(file_content)

    assert "" == result
