#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = """https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
                https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
                worked with Derek to try and figure out and args parsing issue
                Worked with madarp and Daniel on a bunch of shit"""

# +++your code here+++
# Write functions and modify main() to call them


def get_paths(my_path):
    """Return a list of all special paths"""
    special_path_list = []
    all_files = [f for f in os.listdir(
        my_path) if os.path.isfile(os.path.join(my_path, f))]
    pattern = re.compile(r"^[x-z]{2}[z]?__")
    for f in all_files:
        if pattern.match(f):
            special_path_list.append(f)
    return special_path_list


def copy_into(paths, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        shutil.copy(path, dir)


def zip_into(paths, zippath):
    command = ['zip', '-j', zippath]
    command.extend(paths)
    try:
        subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        print(e.output.decode("utf8"))
        exit(e.returncode)


def main(raw_args):
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dir', help='dir stuff')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args(raw_args)
    special_paths = get_paths(args.dir)
    if args.todir:
        copy_into(special_paths, args.todir)
    elif args.tozip:
        zip_into(special_paths, args.tozip)
    else:
        print("\n".join(special_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
