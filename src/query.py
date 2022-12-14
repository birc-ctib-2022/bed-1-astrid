"""Module for querying a genome.

The code in this module is, again, something we haven't seen yet, but you don't
need to understand it to use it. It gives you a table where you can insert
BedLine objects and then access them per chromosome. Create a table and insert
BED lines in it like below, and when you later want to get only the lines relevant
for a given chromosome, you can use the get_chrom() method:

>>> from bed import BedLine
>>> table = Table()
>>> table.add_line(BedLine('chr1', 0, 1, 'foo'))
>>> table.add_line(BedLine('chr2', 0, 1, 'bar'))
>>> table.add_line(BedLine('chr1', 10, 11, 'baz'))
>>> table.get_chrom('chr1')
[BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='foo'), BedLine(chrom='chr1', chrom_start=10, chrom_end=11, name='baz')]
"""

from bed import BedLine
from collections import defaultdict


class Table:
    """Table containing bed-lines."""

    tbl: dict[str, list[BedLine]] # dictionary with chrom name as keys and a list of bedlines as values

    def __init__(self) -> None:      # self? data contained within the Table class is tbl. tbl is assigned at the __init__
        """Create a new table."""    # and assigned as members of self. tbl can then be accessed by the methods
        self.tbl = defaultdict(lambda: [])  # through the self object

    def add_line(self, line: BedLine) -> None:
        """Add line to the table."""
        self.tbl[line.chrom].append(line) # appending is possible because the value for each key is a list.

    def get_chrom(self, chrom: str) -> list[BedLine]:
        """Get all the lines that sits on chrom"""
        return self.tbl[chrom]
