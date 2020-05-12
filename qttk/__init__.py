"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2020 RedFantom
"""
from contextlib import contextmanager
import os
import tkinter as tk


@contextmanager
def chdir(target: str):
    source = os.getcwd()
    try:
        os.chdir(target)
        yield
    finally:
        os.chdir(source)


def load(window: tk.Tk):
    """Load gttk into a Tk instance"""
    path = os.path.dirname(os.path.realpath(__file__))
    with chdir(path):
        window.eval("set dir {0}; source {0}/pkgIndex.tcl".format(path))
        window.tk.call("package", "require", "ttk::theme::tileqt")
