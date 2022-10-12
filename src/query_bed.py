"""Tool for cleaning up a BED file.""" # ?

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this  # why two names?
                           metavar='output',  # name used in help text          # ?
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    # FIXME: put your code here
    
    table = Table()

    for line in args.bed:
        bed_line = parse_line(line)
        table.add_line(bed_line) # self?

    for line in args.query:
        lst = line.split("\t")
        chrom_list = table.get_chrom(lst[0])
        for bedline in chrom_list:
            if bedline.chrom_start >= int(lst[1]) and bedline.chrom_end < int(lst[2]):
                print_line(bedline, args.outfile) # how to print to outfile?


   
   # outfile.close()


# we want all the bedlines that match our query chromosome section.



if __name__ == '__main__':
    main()
