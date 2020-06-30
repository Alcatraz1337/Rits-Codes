'''
Theme:  Optimal Search to search for the best solution for a maze
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

def OptimalSearch(maze_map, start, goal, expCost):
    # expCost indicates the expected cost for making each move
    # Initialize OpenList ClosedList and CostList. 
    # Also notice that function take expected cost for each move as a parameter
    openList = [start, ]
    closedList = []
    cost = 0
    costList = [cost, ]

    # Initialize txt file to save the cost-Openlist and ClosedList
    # Note that cost for moving to every different location is stored in the Cost-OpenList-OpSearch.txt
    # With format: (cost, (x,y))
    colTxt = open("Cost-OpenList-OpSearch.txt", mode= 'w+')
    clTxt = open("ClosedList-OpSearch.txt", mode= 'w+')

    # Set search directions down / up / right / left
    direction = np.array([[1, 0], [-1, 0], [0, 1], [0 , -1]])

    plot_maze(maze_map)

    while openList:
        # Save ClosedList to file
        clTxt.write(str(closedList) + '\n')

        # get the current search state and it's cost, put it into closedList
        s = openList[0]
        openList.remove(s)
        closedList.append(s)
        currentPos = np.array(s)
        cost = costList[0] # cost -> s' cost
        costList.remove(cost)

        if s == goal:
            print("Finished!")
            plt.title("Search Reasult - Using Optimal Search")
            plt.savefig("maze-OpSearch.png")
            plt.show()
            clTxt.write(str(closedList) + '\n')
            break
        else:
            for p in currentPos + direction:
                if tuple(p) not in closedList and maze_map[tuple(p)] != 1:
                    openList.append(tuple(p))
                    plt.quiver(s[1], s[0], (tuple(p)[1]-s[1]), (tuple(p)[0]-s[0]), 
                        angles = 'xy', scale_units = 'xy', scale = 1)
                    costList.append(cost + expCost)
                    # Zip costList and openList together,
                    # so they can be sorted in the same order
                    zippedList = sorted(zip(costList, openList), key= itemgetter(0))
                    
                    # Save Cost-OpenList to file
                    colTxt.write(str(zippedList) + '\n')
                    # Unzip and update
                    costList, openList = zip(*zippedList)
                    # Note that zip() would return *tuple* object, so have to change the type
                    costList = list(costList)
                    openList = list(openList)

if __name__ == "__main__":
    maze = np.loadtxt("maze15x15.txt")
    height, width = maze.shape
    cost = 1
    OptimalSearch(maze, (1, 1), (height - 2, width - 2), cost)

