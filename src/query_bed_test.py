# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from query_bed import main

import filecmp
import os

def test_query_bed() -> None:
    # assert main("data/large.bed", "data/query-1.txt", "text.txt") == "expected-1.txt"  not apllicable 
                                                                                         # since main() takes no arguments

    input_bed = 'data/large.bed'
    input_query = ['data/query-1.txt', 'data/query-2.txt', 'data/query-3.txt']
    out_bedlines = ['data/testout1.txt', 'data/testout2.txt', 'data/testout3.txt']
    exp_bedlines = ['data/expected-1.txt', 'data/expected-2.txt', 'data/expected-3.txt']

    for i in range(3):
        os.system(f"python3 src/query_bed.py {input_bed} {input_query[i]} -o {out_bedlines[i]}")
        assert filecmp.cmp(out_bedlines[i],exp_bedlines[i])
        