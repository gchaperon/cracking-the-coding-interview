[![xc compatible](https://xcfile.dev/badge.svg)](https://xcfile.dev)

# cracking-the-coding-interview
My solutions for the book Cracking the Coding Interview, using Python.

# Tasks
## check-deps
Check that all dependencies are present in the environment.

run: once

```shell
command -v python
command -v pip
```

## configure
Configure dev environment. This includes installing development and testing
dependencies, and pre-commit hooks.

```shell
pip install pre-commit pytest mypy ruff
pre-commit install
```

## test
Run the tests for each exercise.

```shell
pytest
```

# Notes
1. The `legacy` dir is where I've stored an older version of this project. Back
   then, I was extremely motivated and challenged myself to both learn C++ and
   solve the book using it. That motivation did steadily die out, and so I
   archived that version of the project and went back to good ol' trusty simple
   Python. Relatable, ain't it?
