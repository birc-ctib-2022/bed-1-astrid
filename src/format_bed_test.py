# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from cmath import exp
from format_bed import main

import filecmp
import os

infile = 'data/input.bed'
outfile = 'data/testformat.txt'
exp_outfile = 'data/output.bed'

def test_format_bed() -> None:
    os.system(f"python3 src/format_bed.py {infile} {outfile}")
    assert filecmp.cmp(outfile,exp_outfile)

