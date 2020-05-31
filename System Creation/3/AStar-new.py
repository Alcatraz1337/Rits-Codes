'''
Theme:  A* Search to search for the best solution for a maze
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

def AStarSearch(maze_map, start, goal, expCost):
    # Initialize files to save the estCost-Openlist and CloesdList
    # fcost (cost already taken + Est.cost) for moving to different location is stored in totalCost-OpenList-AStarSearch.txt
    # With format:(Tot.cost, (x, y))
    folTxt = open("fCost-OpenList-AStarSearch.txt", mode= 'w+')
    clTxt = open("ClosedList-AStarSearch.txt", mode= 'w+')

    # Initialize OpenList ClosedList and CostList. 
    # Also notice that function take expected cost for each move as a parameter
    openList = [start, ]
    closedList = []
    g_cost = [0]
    h_cost = [manhatannDist(np.array(start), np.array(goal))]
    f_cost = [g_cost[openList.index(start)] + h_cost[openList.index(start)]]

    # Set search directions down / up / right / left
    direction = np.array([[1, 0], [-1, 0], [0, 1], [0 , -1]])

    plot_maze(maze_map)

    while openList:
        # Zip all the lists together and sort them by the value of g_cost
        zippedList = zip(f_cost, g_cost, h_cost, openList)
        zippedList = sorted(zippedList, key= itemgetter(0))

        # Write in the openlist to txt file with f_cost, g_cost, h_cost ahead
        folTxt.write(str(zippedList) + '\n')

        f_cost, g_cost, h_cost, openList = zip(*zippedList)
        
        g_cost = list(g_cost)
        h_cost = list(h_cost)
        f_cost = list(f_cost)
        openList = list(openList)

        s = openList.pop(0)
        g = g_cost.pop(0)
        h_cost.pop(0)
        f_cost.pop(0)
        isBetter = False # A flag to judge if a node in the openlist has been found to have a better g_cost value

        # Write in the closedList to txt file.
        closedList.append(s)
        clTxt.write(str(closedList) + '\n')

        currentPos = np.array(s)

        if s == goal:
            print("Finished!")
            plt.title("Search Result - Using A* Search")
            plt.savefig("maze-AStar.png")
            plt.show()
            break
        # Check every node that is nearby the s (current state / node)
        for p in currentPos + direction:
            if tuple(p) in closedList or maze_map[tuple(p)] == 1:
                continue
            temp_g_cost = g + expCost # Calculate the g_cost for going to p
            if tuple(p) not in openList:
                # It's the first time encounter node p, and draw the route
                g_cost.append(temp_g_cost)
                h_cost.append(manhatannDist(p, np.array(goal)))
                f_cost.append(temp_g_cost + manhatannDist(p, np.array(goal)))
                openList.append(tuple(p))
                plt.quiver(s[1], s[0], (tuple(p)[1]-s[1]), (tuple(p)[0]-s[0]), 
                    angles = 'xy', scale_units = 'xy', scale = 1)
            elif temp_g_cost < g_cost[openList.index(tuple(p))]: # p has already been in the openList, now look for its g_cost and compare
                isBetter = True
            else:
                isBetter = False # p has already been in the openList but it also has a better g_cost, so just leave it
            
            # p has a better g_cost, now draw the new path to the maze and calculate its g_ h_ f_cost
            if isBetter: 
                # Draw the route to the maze
                plt.quiver(s[1], s[0], (tuple(p)[1]-s[1]), (tuple(p)[0]-s[0]), 
                    angles = 'xy', scale_units = 'xy', scale = 1)
                # Update the lists
                idx = openList.index(tuple(p))
                g_cost.remove(idx)
                g_cost.insert(idx, temp_g_cost)
                h_cost.remove(idx)
                h_cost.insert(idx, manhatannDist(p, np.array(goal)))
                f_cost.remove(idx)
                f_cost.insert(idx, temp_g_cost + manhatannDist(p, np.array(goal)))
                

if __name__ == "__main__":
    maze = np.loadtxt("maze15x15.txt")
    height, width = maze.shape
    cost = 1 # Set the cost for each move here
    AStarSearch(maze, (1, 1), (height - 2, width - 2), cost)

