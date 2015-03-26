#!/usr/bin/env python
"""
    make_tree

    uses treelib to create a random binary tree and print it to the screen.

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
from math import log

try:
    import pybst.bstree
    import pybst.draw
except:
    print("You need to install pybst (pip install treelib) for this!")
    sys.exit(1)

def create_random_sequence(length = 10):
    """
        creates a random sequence of integers to insert into the tree

        The sequence goes from 0 to length, but the order of the values will
        be randomly permutated

        input:
            length: an integer representing the length of the random sequence

        output:
            a list of len(length) containing a randomized list of entries
    """

    assert(isinstance(length, int))

    l = range(0, length)
    random.shuffle(l)

    return [(x, True) for x in l]

if __name__ == "__main__":

    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    else:
        length = 10

    sequence = create_random_sequence(length)
    tree = pybst.bstree.BSTree(sequence)
    print("Order of insertion:\n\t{}".format([x[0] for x in sequence]))
    print("Tree's height {}".format(tree.get_height()))
    print("N = {}".format(length))
    print("log(N) = {}".format(log(length, 2)))
    pybst.draw.plot_tree(tree)


