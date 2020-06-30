'''
Theme:  Q-Learning
Name:   LUO Yiming
ID:     2600170541-4
Class:  F2
Group:  D
Note:   I have skipped Q4-1, Q4-1 is simply randomly going through the maze without using
        Q-Table, which means it's a process of creating R-Table for the Q-Learning, so i
        just straight dive into Q4-2, Q4-3 and Q4-4. 
        *To check each result of using different policy, *
        *please change the code from line 201 to line 204.*
        *After the plot stops updating just click on the plot to close it.*
'''

import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import copy
import random
import time
import math


# Policy: Random choice
def randomChoice(pMove):
    if random.random() <= 1 - pMove:
        return 'stay'
    else:
        return random.choice(['up', 'down', 'left', 'right'])


# Policy: Greedy Policy, returns the action with the highest value
def greedy(Q, s):
    # Note that if multiple actions have a same max value, should randomly choose from them
    actionList = []
    for a, v in Q[s].items():
        if v == max(Q[s].values()):
            max_a = a
            actionList.append(max_a)
    return random.choice(actionList)


# Policy: Epsilon-Greedy Policy
# In the Epsilon-Greedy policy, either we select the best action with a probability 1-epsilon
# or we select the actions at random with a probability epsilon:
def eGreedy(Q, s, e):
    if np.random.random() < e:
        return random.choice(list(Q[s].keys()))
    else:
        return greedy(Q, s)


# Policy: Boltzmann Exploration Policy, we select an action based on
# a probability from the Boltzmann distribution.
# T is called a temperature factor, which specifies how many random actions we can explore.
# When T is high, all actions will be explored equally, but when is low, high-rewarding...
# Should note that in the textbook the same parameter is called: Inverse Temperature,
# which is the same as the T in which declared in this function.
def boltzmann(Q, s, t, i, dR):
    t -= i * dR  # Temperature reduces as the process continues. dR means temperature Decrease Rate
    if t > 0:
        actionProbsNumes = []  # Stores the result of Boltzmann Distribution
        denom = 0
        for m in Q[s].values():
            val = math.exp(m / t)
            actionProbsNumes.append(val)
            denom += val
        actionProbs = [x / denom for x in actionProbsNumes
                       ]  # Stores the possibily of each action
        # Choose action base on their possibility.
        # Kind of like Roulette Wheel Selection
        randVal = random.uniform(0, 1)
        probSum = 0
        for i, prob in enumerate(actionProbs):
            probSum += prob
            if randVal <= probSum:
                return list(Q[s].keys())[i]

    # if we are too cold, which means we simply choose randomly from each action
    else:
        return random.choice(list(Q[s].keys()))


def isGoalNearby(pos, goal):
    # Check if goal is around the current position (or state)
    direction = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    for p in np.array(pos) + direction:
        if tuple(p) == goal:
            return True
    return False


def isWall(pos):
    # Check if one position is a wall
    return True if maze[pos] == 1 else False


def initialize(maze_w, maze_h, goal, goalValue, wallPunishment, normalValue):
    # Initialize the Q-Table and Reward Function(R-Table)
    # Type: Dictionary
    # Key: State (tuple)
    # Value: Actions (dictionary)
    Q = {}
    R = {}
    # Type: Dictionary
    # Key: Actions the agent can take (string)
    # Value: Value of action taken by agent (int)
    action = {'stay': 0, 'up': 0, 'down': 0, 'right': 0, 'left': 0}
    for i in range(1, maze_w):
        for j in range(1, maze_h):
            if maze[i, j] == 0:

                Q[(i, j)] = copy.deepcopy(action)
                R[(i, j)] = copy.deepcopy(action)
                if isGoalNearby((i, j), goal):
                    if (i + 1, j) == goal:
                        R[(i, j)]['down'] = goalValue
                    if (i - 1, j) == goal:
                        R[(i, j)]['up'] = goalValue
                    if (i, j + 1) == goal:
                        R[(i, j)]['right'] = goalValue
                    if (i, j - 1) == goal:
                        R[(i, j)]['left'] = goalValue
                else:
                    if isWall((i + 1, j)):
                        R[(i, j)]['down'] = wallPunishment
                    if isWall((i - 1, j)):
                        R[(i, j)]['up'] = wallPunishment
                    if isWall((i, j + 1)):
                        R[(i, j)]['right'] = wallPunishment
                    if isWall((i, j - 1)):
                        R[(i, j)]['left'] = wallPunishment
    return Q, R


# Returns the value of an action
def getReward(R, s, a):
    return R[s][a]


# Go to next position after taking an action
def goToNextState(s, a):
    y, x = s
    if a == 'up':
        return (y - 1, x)
    elif a == 'down':
        return (y + 1, x)
    elif a == 'left':
        return (y, x - 1)
    else:
        return (y, x + 1)


# Get the next state of current state after taking an action
# Used to check if is wall
def getNextState(s, a):
    y, x = s
    if a == 'up':
        return maze[(y - 1, x)]
    elif a == 'down':
        return maze[(y + 1, x)]
    elif a == 'left':
        return maze[(y, x - 1)]
    else:
        return maze[(y, x + 1)]


# Get the max value of Q(S_(t+1), a_(t+1) for every a in A)
def getMaxQ(Q, s):
    return max(Q[s].values())


def showHeatMap(maze, Q):
    height, width = maze.shape
    cmap = plt.get_cmap("YlOrRd")
    image = []
    for y in range(height):
        image_line = []
        for x in range(width):
            if maze[y, x] == 1:
                pixel = (0, 0, 0, 0)
            else:
                pixel = cmap(getMaxQ(Q, (y, x)))
            image_line.append(pixel)
        image.append(image_line)
    plt.imshow(maze, cmap="binary")
    plt.imshow(image)


# Q-Learning Process
def QLearning(maze, start, goal, L, learningRate, discountFactor):
    height, width = maze.shape
    Q, R = initialize(width, height, goal, 10, -1,
                      0)  #<-Change the reward or punishment here
    for i in range(0, L):
        plt.ion()  # Activate interactive mode
        plt.figure(1)
        s = start
        t = 1
        while s != goal:
            # Randomly get action from Policy
            if random.random() <= 0.8:
                # a = randomChoice(0.8)
                # a = greedy(Q, s)
                # a = eGreedy(Q, s, 0.2) #<-Change the epsilon here
                a = boltzmann(Q, s, 100, i, 1)
            else:
                a = 'stay'
            if getNextState(s, a):  # Check if next pos is wall or not
                nextPos = s  # If is wall, stay
            else:
                nextPos = goToNextState(s, a)  # Set S_(t+1)
            Q[s][a] = Q[s][a] + learningRate * (
                R[s][a] + discountFactor * getMaxQ(Q, nextPos) - Q[s][a]
            )  # Update Q-Table
            s = nextPos  # Move the agent
            t += 1
        plt.clf()
        plt.title("Trial No:" + str(i + 1))
        showHeatMap(maze, Q)
        plt.pause(0.001)
        i += 1
    plt.waitforbuttonpress()


if __name__ == '__main__':
    maze = np.loadtxt("testmaze.txt")
    height, width = maze.shape
    QLearning(maze, (1, 1), (height - 2, width - 2), 100, 0.1, 0.9)