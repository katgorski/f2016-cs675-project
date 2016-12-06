#!/usr/bin/env python2

from sys import argv

script, error_f = argv

lines = 0
error_sum = 0
with open(error_f) as f:
    for line in f:
        lines += 1
        error_sum += float(line.strip())

print(error_sum / lines)
