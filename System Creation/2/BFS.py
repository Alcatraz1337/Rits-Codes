'''
Theme:  Breadth-First Search used to search for posible routes in a Maze
Name:   LUO Yiming
ID:     2600170541-4
Class:  F2
Group:  D
Note:   Please download all the file needed to run this program. 
        And make sure to put them in the same folder. Thank you very much
        Files needed: maze15x15.txt
        Files outputed: OpenList-BFS.txt / ClosedList-BFS.txt
'''

import numpy as np
import matplotlib.pyplot as plt

def BFS(maze_map, start, goal):
    # Initialize OpenList and ClosedList
    openList = [start, ]
    closedList = []

    # Initialize txt file to write in OpenList and ClosedList
    olTxt = open("OpenList-BFS.txt", mode = 'w+')
    clTxt = open("ClosedList-BFS.txt", mode = 'w+')

    # Set moving directions left/ right / up / down - also mean search priority
    direction = np.array([[0, -1], [0, 1], [1, 0], [-1, 0]])

    plot_maze(maze_map)
    
    while openList:
        # Print OpenList into file: OpenList-BFS.txt
        strToWrite = str(openList) + '\n'
        olTxt.write(strToWrite)
        # Print ClosedList into file: ClosedList-BFS.txt
        strToWrite = str(closedList) + '\n'
        clTxt.write(strToWrite)

        # OpenList is a Queue, which means using FIFO method
        s = openList[0] # s -> current state / position
        openList.remove(s)
        closedList.append(s)
        currentPos = np.array(s) # change s into np.ndarray for later use
        if s == goal:
            print("Finished")
            # Update the final lists to the txt files
            strToWrite = str(openList) + '\n'
            olTxt.write(strToWrite)
            strToWrite = str(closedList) + '\n'
            clTxt.write(strToWrite)
            plt.title("Search Result - Using BFS Method")
            plt.savefig("maze-BFS.png")
            plt.show()
            break
        else:
            nextPos = currentPos + direction
            for p in nextPos:
                if tuple(p) not in closedList and maze_map[tuple(p)] != 1:
                    openList.append(tuple(p))
                    plt.quiver(tuple(currentPos)[1], tuple(currentPos)[0], (tuple(p)[1]-tuple(currentPos)[1]), (tuple(p)[0]-tuple(currentPos)[0]), 
                                angles = 'xy', scale_units = 'xy', scale = 1)

def plot_maze(maze_map, save_file=None):
    height, width = maze_map.shape
    plt.imshow(maze_map, cmap="binary")
    plt.xticks(rotation=90)
    plt.xticks(np.arange(width), np.arange(width))
    plt.yticks(np.arange(height), np.arange(height))
    plt.plot(1, 1, "D", color = "tab:red", markersize = 10)
    plt.plot(width - 2, width - 2, "D", color = "tab:green", markersize = 10)

    plt.gca().set_aspect('equal')

if __name__ == "__main__":
    maze = np.loadtxt("maze15x15.txt")
    height, width = maze.shape
    BFS(maze, (1,1), (height - 2, width - 2))
    
