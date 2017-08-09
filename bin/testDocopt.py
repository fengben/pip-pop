"""
Usage:
    testDocopt.py [-varh] [FILE] ...
    testDocopt.py (-left|-right) CORRECTION FILE

Arguments:
    FILE    optional input file
    CORRECTION correction angle,nedds FILE, --left or --right to be present

Options:
    -h --help   show this
    -v          verbose mode
    -q          quite mode
    -r          make report
    --left      use left-hand side
    --right     use right-hand side

Examples:
    testDocopt.py -v 123.txt
"""

from docopt import docopt
if __name__=='__main__':
    arguments=docopt(__doc__)
    print(arguments)