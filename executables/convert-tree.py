#!/usr/bin/env python

"""
    Bulk file copy and AVI conversion utility for AMOS.
    Requires a YAML configuration file (can be overridden with arguments).
    Version 2023.03.16
    Ⓒ Kvík, 2021-2023

    For use in production you should create an EXE file with `pyinstaller.exe --onefile convert-tree.py`,
    see pyinstaller documentation.
"""

from classes.tree import DirectoryConvertor

DirectoryConvertor.run()
