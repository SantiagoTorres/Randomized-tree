#!/usr/bin/env python
import matplotlib
from matplotlib.pyplot import plot, show, savefig, legend
import matplotlib.pyplot as pp
import numpy as np
from math import log, pow

C = 2.01353641000000003 

def load_log(filename = 'means.log'):

    sizes = []
    with open(filename) as fp:
        for line in fp:
            try:
                fields = line.strip().split(" ")
                size = int(fields[0].strip("[ ]"))
                height = float(fields[-1])
                sizes.append((size, height))

            except:
                import pdb; pdb.set_trace()
    return sizes


def main():

    data = load_log()
    data = data[1:]
    indexes = [x[0] for x in data]
    values = [x[1] for x in data]
    logvalues = [log(x[0], 2) for x in data]
    rootvalues = [pow(x[0], .5) for x in data]
    clogvalues = [pow(x,1.325) for x in logvalues]

    plot(indexes, values, color = 'red', label = 'Randomized Tree Height',
            markevery= (10, 10), marker = '>')

#    plot(indexes[::10], values[::10], label='Randomized Tree Height', color = 'red',  marker ='>')

    plot(indexes, logvalues, label = 'logaritmic growth', color = 'green', 
            markevery = (10, 10), marker ='^')

    plot(indexes, clogvalues, label='log^1.325 growth', color = 'blue', 
            markevery = (10, 10), marker = 'x')

#    plot(indexes, rootvalues, color = 'black')
#    plot(indexes[::10], rootvalues[::10], label = 'N^(1/2) growth', color = 'black',  marker = '<')





    pp.title(
        'Mean tree height for different tree sizes', fontsize=60)

    pp.xlabel("Tree Size", fontsize=50)
    pp.ylabel("Tree height", fontsize=50)

    legend(loc='lower right', prop={'size':36})

    show() 


if __name__ == '__main__':
    
    main()


