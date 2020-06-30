import matplotlib.pyplot as plt
import numpy as np

def getMaxQ(Q, s):
    return max(Q[s].values())

maze = np.loadtxt("testmaze.txt")

def showHeatMap(maze, Q):
    height, width = maze.shape
    cmap = plt.get_cmap("Greens ")
    image = []
    for y in range(height):
        image_line = []
        for x in range(width):
            if maze[y, x] == 1:
                pixel = (0,0,0,0)
            else:
                pixel = cmap(getMaxQ(Q, (y, x)))
            image_line.append(pixel)
        image.append(image_line)
    plt.imshow(maze, cmap="binary")
    plt.imshow(image)