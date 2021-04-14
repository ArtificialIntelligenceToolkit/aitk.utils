# -*- coding: utf-8 -*-
# ***********************************************************
# aitk.utils: Python AI utils
#
# Copyright (c) 2020 AITK Developers
#
# https://github.com/ArtificialIntelligenceToolkit/aitk.utils
#
# ***********************************************************

import os
import numpy as np

from .utils import get_file

_filename = get_file(
    "digits6x6.zip",
    "https://media.githubusercontent.com/media/Calysto/conx-data/master/digits6x6/digits6x6.zip",
    extract=True,
)

DATA_DIR = os.path.splitext(_filename)[0]

def get():
    """Each digit is represented by a 6x6 grid of 1's and 0's separated by blank lines."""
    filename = DATA_DIR + ".data"
    fp = open(filename, "r")
    data = []
    while True:
        digit = []
        line = fp.readline()
        while len(line) != 0 and (line[0] == '0' or line[0] == '1'):
            line.strip()
            values = line.split()
            digit += [int(v) for v in values]
            line = fp.readline()
        if len(line) == 0:
            break
        if len(digit) > 0:
            data.append(digit)
    return np.array(data)    