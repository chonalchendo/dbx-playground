# run format tasks
[group('format')]
format: format-python-import format-python-source format-sql-dbt

# format python code import
[group('format')]
format-python-import:
    uv run ruff check --select=I --fix {{SOURCES}} {{TESTS}}

# format python code source
[group('format')]
format-python-source:
    uv run ruff format {{SOURCES}} {{TESTS}}

# format sql code dbt
[group('format')]
format-sql-dbt:
    uv run sqruff lint {{DBT}}
