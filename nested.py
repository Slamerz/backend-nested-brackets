#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Your Github Username"

import sys
import re


def main(args):
    f = open("input.txt", 'r').read()
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
    new_f = open("output.txt", "w+")
    for l in results:
        new_f.write(str(l)+"\n")
    print("Jobs Done")


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


# (  )
# [  ]
# {  }
# <  >
# (*  *)
if __name__ == '__main__':
    main(sys.argv)
