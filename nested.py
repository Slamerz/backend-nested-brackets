#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Receives an input file, and evaluates if each line is currently using valid brackets, and if not the length of the
line split at where it is invalid. """
__author__ = "slamerz"

import sys
import re


def main(args):
    check_file("input.txt")
    print("Jobs Done")


def check_file(file_name):
    f = open(file_name, 'r').read()
    results = []
    for line in f.split('\n'):
        # creates a list of only (* *) ( ) [ ] < > { } from the file
        brackets = re.findall(r"(\(\*|\*\)|[()<>{}[\]])", line)
        b = [m.end(0) for m in re.finditer(r"(\(\*|\*\)|[()<>{}[\]])", line)]
        valid = is_valid(brackets)
        r = "None"
        if valid[0]:
            r = "YES"
        elif not valid[1]:
            r = "NO " + str(len(line) + 1 - len(re.findall(r"\(\*|\*\)", line)))
        else:
            last = b[valid[1]]
            err = "".join(line[0: last])
            p_length = len(re.findall(r"\(\*|\*\)", err))
            r = "NO " + str(len(err) - p_length)
        results.append(r)
    write_output(results)


def is_valid(brackets):
    current_brackets = []
    open_brackets = {"(*", "<", "{", "[", "("}
    brackets_dict = {"*)": "(*", ">": "<", "]": "[", "}": "{", ")": "("}

    for index, bracket in enumerate(brackets):
        if bracket in open_brackets:
            current_brackets.append(bracket)
        elif not current_brackets:
            return [False, index]
        elif current_brackets.pop() != brackets_dict[bracket]:
            return [False, index]
    return [not current_brackets, None]


def write_output(results_list):
    new_f = open("output.txt", "w+")
    for l in results_list:
        new_f.write(str(l) + "\n")


# (  )
# [  ]
# {  }
# <  >
# (*  *)
if __name__ == '__main__':
    main(sys.argv)
