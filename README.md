# Precommit - Clean sql files

## Description

Precommit hook that removes extra lines at the end of a sql file (runs only on `sql` files).
This is needed to keep the file clean so that it can run in Disneystreaming's airflow instance.

The same functionality is in the `end-of-file-fixer`.  The description in [pre-commit docs](https://github.com/pre-commit/pre-commit-hooks/tree/5d1ab6d7f3e8f928c896232d2fb0ff95b3563ca6#end-of-file-fixer)
says that it adds a new line rather than removing lines

## Usage

Add this to your `.pre-commit-config.yaml` file

```yaml
repos:
-   repo: https://github.bamtech.co/cupjohn/pre-commit-sql-remove-lines.git
    rev: v1
    hooks:
    -   id: end-of-file-sql
```

## Testing

There is a `.justfile` which is like a `makefile`.
Instead of targets they are called recipes.
Need to brew install `just`  : `brew install just`

To get started you will need to create the virtualenv:
- `just install-virtualenv`

For running tests locally:
- `just run-pytest`

To test the functionality like it would run in pre-commit
- open another terminal, create a new dir and set up git repo in that dir (`git init`)
- create a file in the other dir
- `git add . && pre-commit try-repo ../disney_precommit_sql_file end-of-file-sql`
 - [instructions at pre-commit doc page](https://pre-commit.com/index.html#developing-hooks-interactively)
