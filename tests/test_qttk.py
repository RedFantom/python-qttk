"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2020 RedFantom
"""
import tkinter as tk
from tkinter import ttk
import qttk
from unittest import TestCase
import sys


def printf(string, end="\n"):
    sys.__stdout__.write(string + end)
    sys.__stdout__.flush()


class TestQTTK(TestCase):
    WIDGETS = [
        "Label",
        "Treeview",
        "Button",
        "Frame",
        "Notebook",
        "Progressbar",
        "Scrollbar",
        "Scale",
        "Entry",
        "Combobox"
    ]

    def test_widget_creation(self):
        try:
            import signal
        except ImportError:
            pass
        if "signal" not in locals() or not hasattr(signal, "alarm"):
            return
        for widget in self.WIDGETS:
            window = tk.Tk()
            style = ttk.Style(window)
            qttk.load(window)
            style.theme_use("tileqt")
            signal.alarm(5)
            printf("Testing {}".format(widget), end=" - ")
            getattr(ttk, widget)(window).pack()
            window.update()
            window.destroy()
            signal.alarm(0)
            printf("SUCCESS")
