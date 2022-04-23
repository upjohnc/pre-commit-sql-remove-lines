import pytest

from precommit_sql_clean import hook_check_file, remove_endlines


def test_basic_file_no_extra_lines():
    file_content = "select *"
    result = remove_endlines(file_content)

    assert file_content == result


def test_basic_file_with_extra_lines():
    file_content_base = "select *"
    file_content = f"{file_content_base}\n  \n"
    result = remove_endlines(file_content)

    assert file_content_base == result


def test_empty_file_with_extra_lines():
    file_content = ""
    result = remove_endlines(file_content)
    assert file_content == result


def test_blank_lines_file_with_extra_lines():
    file_content = "    "
    result = remove_endlines(file_content)

    assert "" == result


def test_basic_file_no_extra_lines_pass(fs):
    file_name = "/var/data/xx1.txt"
    file_content = "select *"
    fs.create_file(file_name, contents=file_content)
    hook_result = hook_check_file(file_name)
    with open(file_name) as f:
        file_result = f.read()

    with pytest.assume:
        assert file_result == file_content

    with pytest.assume:
        assert hook_result == 1


def test_basic_file_with_extra_lines_fail(fs):
    file_name = "/var/data/xx1.txt"
    file_content_base = "select *"
    file_content = f"{file_content_base}\n  \n"
    fs.create_file(file_name, contents=file_content)
    hook_result = hook_check_file(file_name)

    with open(file_name) as f:
        file_result = f.read()

    with pytest.assume:
        assert file_result == file_content_base

    with pytest.assume:
        assert hook_result == 0
