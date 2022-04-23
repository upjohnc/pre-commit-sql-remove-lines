# Precommit - Clean sql files

## Description

Precommit hook that removes extra lines at the end of a sql file.
This is needed to keep the file clean so that it can run in Disneystreaming's airflow instance.

## Usage


## Testing

has pytest - run with just command

need to brew install `just`  : `brew install just`
run commands like you do in make with `just run-pytest`

test locally:
open another terminal and set up git repo (`git init`)
create a file
`git add . && pre-commit try-repo ../disney_precommit_sql_file end-of-file-sql`
[instructions at pre-commit doc page](https://pre-commit.com/index.html#developing-hooks-interactively)
