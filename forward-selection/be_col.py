#!/usr/bin/env python

from __future__ import print_function
from re import split
from sys import argv

def standardize_labels(label_f):
    with open(label_f) as f:
        data = [[int(j) for j in split(r'\s+', line.strip())] for line in f.readlines()]
    label_dict = {datum[1]: datum[0] for datum in data}
    return label_dict

try:
    script, predict_labels, true_labels, j = argv
except ValueError:
    print("Please run in the format script predicted_labels true_labels.")
    quit()

pmap = standardize_labels(predict_labels)
tmap = standardize_labels(true_labels)

a = 0
b = 0
c = 0
d = 0

for line in pmap:
    if pmap[line] == 0 and tmap[line] == 0:
        a += 1
    elif pmap[line] == 0 and tmap[line] == 1:
        c += 1
    elif pmap[line] == 1 and tmap[line] == 0:
        b += 1
    elif pmap[line] == 1 and tmap[line] == 1:
        d += 1

#print("a = %d, b = %d, c = %d, d = %d" % (a, b, c, d))
#ber = 0.5 * (b / (a + b) + c / (c + d))
print(j, ber)
