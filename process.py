#!/usr/bin/env python
#
import sys
import fileinput

from core import segment

def get_path(filename):
    return 'data/' + filename

for line in fileinput.input(inplace=True, backup='.bak', files=map(get_path, sys.argv[1:])):
    print(segment(line), end='')  # this goes to the current file
