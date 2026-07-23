import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict

import numpy
import sortedcontainers

def simulate_coding_framework(list_of_lists):
    """
    Simulates a coding framework operation on a list of lists of strings.

    Parameters:
    list_of_lists (List[List[str]]): A list of lists containing strings.
    """

    database = FileDatabase()
    results = []

    for data in list_of_lists:
        action: str = data[0]
        args: list = data[1:]
        
        if action == "FILE_UPLOAD":
            results.append(database.FILE_UPLOAD(*args))
        elif action == "FILE_GET":
            size = database.FILE_GET(*args)
            results.append(f"got {args[0]}")
        elif action == "FILE_COPY":
            results.append(database.FILE_COPY(*args))
        elif action == "FILE_SEARCH":
            results.append(database.FILE_SEARCH(*args))
        else:
            continue

    return results


class File:

    def __init__(self, name, size):
        self.name: str = name
        self.size: str = size

    def __lt__ (self, other):
        if self.size != other.size:
            return self._get_file_size_int() < other._get_file_size_int()
        else:
            return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name and self.size == other.size

    def _get_file_size_int(self):
        return int(self.size.split("kb")[0])

class FileDatabase:

    def __init__(self):
        self.files: list[File] = []
        return

    def _get_file_name_list(self):
        if len(self.files) != 0:
            return [file.name for file in self.files]
        else:
            return []

    def FILE_UPLOAD(self, file_name:str, file_size:str):
        if file_name in self._get_file_name_list():
            raise RuntimeError("File already exists on server")
        else:
            self.files.append(File(file_name, file_size))

            return f"uploaded {file_name}"

    def FILE_GET(self, file_name:str):
        if file_name in self._get_file_name_list():
            idx = self._get_file_name_list().index(file_name)
            return self.files[idx].size

    def FILE_COPY(self, source, dest):
        if source not in self._get_file_name_list():
            raise RuntimeError("Source file does not exist in database")

        if dest in self._get_file_name_list():
            idx = self._get_file_name_list().index(file_name)
            self.files.pop(idx)

        size = self.files[self._get_file_name_list().index(source)].size

        self.files.append(File(dest, size))

        return f"copied {source} to {dest}"

    def FILE_SEARCH(self, prefix):
        top_ten_files = []
        for file in self.files:
            if len(top_ten_files) >= 10:
                return [file.name for file in top_ten_files]

            if file.name.startswith(prefix):
                top_ten_files.append(file)
        
        top_ten_files.sort(reverse=True)

        names = [file.name for file in top_ten_files]

        return f"found {str(names)}"

