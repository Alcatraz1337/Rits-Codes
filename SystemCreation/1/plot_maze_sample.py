# ライブラリのインポート
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# 迷路を定義
# Define a maze
maze = np.array(
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
    )

# 迷路の高さと幅を取得
# Get the height and width of the maze
height, width = maze.shape

# 迷路のプロット
# Plot the maze
plt.imshow(maze, cmap="binary")

# 縦横比を1:1にする
# Set aspect to 1:1
plt.gca().set_aspect("equal")

# x軸のラベルを90度回転
# Rotate texts of x-axis
plt.xticks(rotation=90)

# x軸の目盛りを全て表示
# Show the all x-axis ticks
plt.xticks(np.arange(width), np.arange(width))

# y軸の目盛りを全て表示
# Show the all y-axis ticks
plt.yticks(np.arange(height), np.arange(height))

# 表示
# Show the results of plot
plt.show()
