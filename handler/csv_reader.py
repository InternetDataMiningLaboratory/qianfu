# -*- coding: utf-8 -*-
#
# Author: jimin.huang
#
'''
    Read The Data From CSV format files.
'''
def read(filename):
    datum = []

    # Open file
    with open(filename) as f:
        for line in f:
            data = line.split(';')
            datum.append(data)

    return datum
