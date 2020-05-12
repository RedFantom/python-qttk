"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2020 RedFantom
"""
try:
    from skbuild import setup
    from skbuild.command.build import build
except ImportError:
    print("scikit-build is required to build this project")
    print("install with `python -m pip install scikit-build`")
    raise


def read(file_name):
    with open(file_name) as fi:
        contents = fi.read()
    return contents


setup(
    name="qttk",
    version="0.1.0",
    packages=["qttk"],
    description="Qt theme for Tkinter/ttk",
    author="The qttk/tile-qt authors",
    url="https://github.com/RedFantom/python-qttk",
    download_url="https://github.com/RedFantom/python-qttk/releases",
    license="GNU GPLv3",
    long_description=read("README.md"),
    zip_safe=False,
    install_requires=["scikit-build"],
)
