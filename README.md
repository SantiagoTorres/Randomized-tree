# Randomized-tree
A small script to draw a randomized BST of arbitrary length

## How to get this
clone or download the zip file and get the dependencies:

```Bash
$ pip install pybst
$ pip install matplotlib
$ pip install networkx
```

## How to run:

```Bash
$ python make_tree.py [size]
```

It defaults for a size of 10 and I've tested it up to 50. Feel free to play
around and tell me if there are any problems.

### An experiment on randomized tree sizes

There are two scripts:

* Mean tree sizes
* plot_tree_sizes

You can use them to programatically test the average tree height for a randomized tree.

The experiment should take a while, since it creates about five million trees
of sizes up to n=500, but you should be able to see a really neat plot of how
the size of a randomized tree is actually O(logn). It actually seems to be
O(log(n)^1.33).

If you don't want to run the experiment yourself, you can still look at the
plot in the plots folder to see the results.

