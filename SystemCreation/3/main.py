'''
Theme:  Option Question 3-4
Name:   LUO Yiming
ID:     2600170541-4
Class:  F2
Group:  D
Note:   Please download all the file needed to run this program. 
        And make sure to put them in the same folder. Thank you very much
        Files needed: maze15x15.txt 
'''

from AStar import *
from AStarWithWrongHx import AStarSearchIncorrect
from OptimalSearch import OptimalSearch
from BestFirstSearch import BFSearch

if __name__ == "__main__":
    maze = np.loadtxt("maze15x15.txt")
    height, width = maze.shape

    OptimalSearch(
        maze, (1, 1), (height - 2, width - 2), expCost=1
    )  #<-change expCost to set a different cost for making each move
    BFSearch(maze, (1, 1), (height - 2, width - 2))
    AStarSearch(maze, (1, 1), (height - 2, width - 2),
                expCost=1)  #<-same as above
    AStarSearchIncorrect(maze, (1, 1), (height - 2, width - 2), expCost=1)
