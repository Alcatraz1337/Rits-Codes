import numpy as np
import itertools
import operator

maze = np.arange(25).reshape(5,5)
print(maze)
all_points = list(itertools.product(range(0, 5), range(0, 5)))
print(all_points)
s = (1,1)
pos = np.array(s)
direction = np.array([[0, -1], [0, 1], [1, 0], [-1, 0]])
print(pos + direction)

openlist = [s, ]
if openlist is []:
    print(openlist)
closedlist = []
closedlist.append(openlist.pop())
print(openlist)
if (1,1) in closedlist:
    print(closedlist)


for i in range(10):
    print(i)
    if i == 5:
        break





    