# 迷路作成プログラム
#
# 実行方法
# $ python make_maze.py
#
# 本プログラムは以下のサイトを参考に作成しています．
# 壁伸ばし法 - Algoful [ http://algoful.com/Archive/Algorithm/MazeExtend ]
#
# 作成者　尾崎僚

import numpy as np
import matplotlib.pyplot as plt
import itertools
import random

def plot_maze(maze_map, save_file=None):
    height, width = maze_map.shape
    plt.imshow(maze_map, cmap="binary")
    plt.xticks(rotation=90)
    plt.xticks(np.arange(width), np.arange(width))
    plt.yticks(np.arange(height), np.arange(height))

    plt.gca().set_aspect('equal')
    if save_file is not None:
        plt.savefig(save_file)
    else:
        plt.show()


def make_maze(height, width):
    if height < 5 or width < 5 or height % 2 == 0 or width % 2 == 0:
        print("迷路の高さ・幅は5以上の奇数でなければなりません．")
        return None

    maze = np.zeros((height, width), dtype=int)

    # 上下左右の壁を設定
    maze[ 0,  :] = 1
    maze[-1,  :] = 1
    maze[ :,  0] = 1
    maze[ :, -1] = 1

    all_points = list(itertools.product(range(2, height-2, 2), range(2, width-2, 2)))

    while all_points: # while all_points have element
        point = random.choice(all_points)
        wall_points = extend_wall(maze, point)
        for wp in wall_points:
            all_points.remove(wp)

    return maze

def extend_wall(maze, start):
    # left, right, up, down
    d_mat = np.array([[0, -2], [0, 2], [-2, 0], [2, 0]])
    wall_points = [start, ]
    wall_points_stack = [start, ]
    maze[start] = -1
    current = np.array(start)
    while True:
        next_v = np.array([maze[tuple(p)] for p in (current + d_mat)])
        if np.all(next_v == -1):
            current = np.array(wall_points_stack.pop())
            continue
        else:
            d_idx = random.choice(np.where(next_v != -1)[0])
            maze[tuple(current + (d_mat[d_idx]//2))] = -1
            p = tuple(current+d_mat[d_idx])
            if maze[p] == 1:
                break
            maze[p] = -1
            wall_points.append(p)
            wall_points_stack.append(p)
            current = current + d_mat[d_idx]

    maze[maze == -1] = 1
    return wall_points

if __name__ == "__main__":
    while True:
        height = int(input("迷路の高さ >> "))
        width = int(input("迷路の幅 >> "))
        if height < 5 or width < 5 or height % 2 == 0 or width % 2 == 0:
            print("迷路の高さ・幅は5以上の奇数でなければなりません．")
            print()
            continue
        else:
            break
    while True:
        maze = make_maze(height, width)
        plot_maze(maze)
        if input("この迷路を保存しますか？ (y/n) >> ") == "y":
            name = input("迷路の名前(.txtを除く) >> ")
            np.savetxt(f"{name}.txt", maze, fmt="%d")
            plot_maze(maze, save_file=f"{name}.png")
            print(f"作成した迷路を{name}.pngと{name}.txtに保存しました．")
        print()
        if input("同じ条件でもう一度迷路を生成しますか？ (y/n) >> ") == "y":
            continue
        else:
            break
    print("処理を終了します．")
