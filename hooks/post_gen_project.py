#!/usr/bin/env python
import pathlib
import subprocess

def git_init():
    subprocess.run(["git", "init"])

def setup_venv():
    subprocess.run(["pyenv", "local", "{{ cookiecutter.python_version }}"])
    command = """poetry add
        black -G dev
        isort -G dev
        flake8 -G dev
        mypy -G dev
        pytest -G dev"""
    command = command.replace("\n        ", " ")
    subprocess.run(command.split(" "))
    subprocess.run("poetry", "install")


if __name__ == '__main__':
    git_init()
    setup_venv()
