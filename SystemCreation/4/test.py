import numpy as np
import copy
import random
import math

maze = np.loadtxt("testmaze.txt")
height, width = maze.shape


def isGoalNearby(pos, goal):
    # Check if goal is around the current position (or state)
    direction = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    for p in np.array(pos) + direction:
        if tuple(p) == goal:
            return True
    return False


def hasValue(pos):
    # Check if one position has a value
    # Means a position is a wall or is final goal
    return True if maze[pos] != 0 else False


def isWall(pos):
    # Check if one position is a wall
    return True if maze[pos] == 1 else False


def initialize(maze_w, maze_h, goal, goalValue, wallPunishment, normalValue):
    # Initialize the Q-Table and Reward Function
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


# Action Policy: Random choice
def action_randomChoice(pMove):
    if random.random() <= 1 - pMove:
        return 'stay'
    else:
        return random.choice(['up', 'down', 'left', 'right'])


# Get the next state of current state after taking an action
def getNextState(s, a):
    x, y = s
    if a == 'up':
        return maze[(x - 1, y)]
    elif a == 'down':
        return maze[(x + 1, y)]
    elif a == 'left':
        return maze[(x, y - 1)]
    else:
        return maze[(x, y + 1)]


def getMaxQ(Q, s):
    return max(Q[s].values())


#  # Set search directions down / up / right / left
#direction = np.array([[1, 0], [-1, 0], [0, 1], [0 , -1]])
d = {'a': 1, 'b': 3, 'c': 2, 'd': 3}


def greedy(d):
    actionList = []
    for a, v in d.items():
        if v == max(d.values()):
            max_a = a
            actionList.append(max_a)
    return random.choice(actionList)


def eGreedy(Q, s, e):
    if np.random.random() < e:
        return random.choice(['stay', 'up', 'down', 'left', 'right'])
    else:
        return greedy(Q, s)


val = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(list(val.keys())[2])




def boltzmann(Q, s, t):
    if t > 0:
        actionProbsNumes = []
        denom = 0
        for m in Q[s].values():
            val = math.exp(m / t)
            actionProbsNumes.append(val)
            denom += val
        actionProbs = [x / denom for x in actionProbsNumes]
    # Randomly choose action base on their possibility.
    randVal = random.uniform(0, 1)
    probSum = 0
    for i, prob in enumerate(actionProbs):
        probSum += prob
        if randVal <= probSum:
            return list(Q[s].keys())[i]
    
    # if we are too cold, which means we simply choose randomly from each action
    else:
        return random.choice
