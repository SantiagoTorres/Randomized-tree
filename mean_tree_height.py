#!/usr/bin/env python
"""
    mean_tree_height

    uses pybst to create a random binary trees and get their heights, then we
    get the mean height of all of the tree

    A number N of nodes can be inputted from the terminal.

    <Author>
        Santiago Torres

    <Date>
        Whatever

    <License>
        Beerware
"""
import sys
import random
from make_tree import create_random_sequence
from math import log, pow
import logging
import logging.handlers

LOG_FILENAME = 'means.log'

# Set up a specific logger with our desired output level
logger = logging.getLogger('mean_trees')
logger.setLevel(logging.INFO)

# Add the log message handler to the logger
handler = logging.FileHandler(LOG_FILENAME)


logger.addHandler(handler)

NUMBER_OF_TREES = 10000
TREE_RANGE = range(0, 500)
C = 2.1353641000000003 

try:
    import pybst.bstree
    import pybst.draw
except:
    print("You need to install pybst (pip install treelib) for this!")
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    else:
        length = 10
   
    total_height = 0
    for j in TREE_RANGE:
        for i in range(0, NUMBER_OF_TREES):

            sequence = create_random_sequence(j)
            tree = pybst.bstree.BSTree(sequence)
            total_height += tree.get_height()

        total_height /= float(NUMBER_OF_TREES)
    #   temp_c = 0
        logger.info("[{}] Mean tree height: {}".format(j, total_height))
#    print("N = {}, log(N) = {}".format(len(sequence), pow( C* length, .5)))
#   print("log(n)/height = {}".format(pow(C * length, .5)/total_height))
#   temp_c = pow(total_height, 2)/length
#   print("C should be: {}".format(temp_c))

