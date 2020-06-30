'''
Theme:  Best-First Search to search for the best solution for a maze
Name:   LUO Yiming
ID:     2600170541-4
Class:  F2
Group:  D
Note:   Please download all the file needed to run this program. 
        And make sure to put them in the same folder. Thank you very much
        Files needed: maze15x15.txt 
'''

import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def plot_maze(maze_map, save_file=None):
    height, width = maze_map.shape
    plt.imshow(maze_map, cmap="binary")
    plt.xticks(rotation=90)
    plt.xticks(np.arange(width), np.arange(width))
    plt.yticks(np.arange(height), np.arange(height))
    plt.plot(1, 1, "D", color = "tab:red", markersize = 10)
    plt.plot(width - 2, width - 2, "D", color = "tab:green", markersize = 10)

    plt.gca().set_aspect('equal')

# Calculate the Manhatann Distance between two points
# Note: Both a and b are np.ndarray type!
def manhatannDist(a, b):
    return np.sum(np.abs(a - b))

def BFSearch(maze_map, start, goal):
    # Initialize files to save the estCost-Openlist and CloesdList
    # Estimated cost for moving to every location is stored in estCost-OpenList-BFSearch.txt
    # With format: (Est.Cost, (x, y))
    ecolTxt = open("estCost-OpenList-BFSearch.txt", mode= 'w+')
    clTxt = open("ClosedList-BFSearch.txt", mode= 'w+')

    # Initialize OpenList ClosedList and CostList. 
    
    openList = [start, ]
    closedList = []
    estCost = manhatannDist(np.array(start), np.array(goal))
    estCostList = [estCost, ]

    # Set search directions down / up / right / left
    direction = np.array([[1, 0], [-1, 0], [0, 1], [0 , -1]])
    plot_maze(maze_map)

    while openList:
        # get the current search state and it's cost, put it into closedList
        s = openList[0]
        openList.remove(s)
        closedList.append(s)
        clTxt.write(str(closedList) + '\n')
        currentPos = np.array(s)
        cost = estCostList[0] # cost stands for -> s' cost
        estCostList.remove(cost)

        if s == goal:
            print("Finished!")
            plt.title("Search Result - Using Best-First Search")
            plt.savefig("maze-BFSearch.png")
            plt.show()
            break
        else:
            for p in currentPos + direction:
                if tuple(p) not in closedList and maze_map[tuple(p)] != 1:
                    openList.append(tuple(p))
                    plt.quiver(s[1], s[0], (tuple(p)[1]-s[1]), (tuple(p)[0]-s[0]), 
                        angles = 'xy', scale_units = 'xy', scale = 1)
                    estCostList.append(manhatannDist(p, np.array(goal)))
                    # Zip estCostList and openList together,
                    # so they can be sorted in the same order
                    zippedList = sorted(zip(estCostList, openList), key=itemgetter(0))
                    ecolTxt.write(str(zippedList) + '\n')
                    # Unzip and update
                    estCostList, openList = zip(*zippedList)
                    # Note that zip() would return *tuple* object, so have to change the type
                    estCostList = list(estCostList)
                    openList = list(openList)

if __name__ == "__main__":
    maze = np.loadtxt("maze15x15.txt")
    height, width = maze.shape
    
    BFSearch(maze, (1, 1), (height - 2, width - 2))

