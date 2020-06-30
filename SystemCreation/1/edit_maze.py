# 迷路編集プログラム
#
# 実行方法
# $ python edit_maze.py
#
# 編集したい迷路が既にある場合
# $ python edit_maze.py [編集したい迷路のファイル名(.txtを含む)]
#
# クリックで壁/通路の切り替えができる
# matplotlibを閉じ，保存名を入力すると迷路ファイル(.txt)と迷路画像(.png)で保存される
#
# 作成者　尾崎僚

import numpy as np
import matplotlib.pyplot as plt
import itertools
import sys

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
        plt.pause(0.001)

def onclick(event):
    x, y = event.xdata, event.ydata
    if 0.5 < x < (width - 1.5) and 0.5 < y < (height - 1.5):
        round_x = int(x + 0.5)
        round_y = int(y + 0.5)
        edit_point = (round_y, round_x)

        if event.button == 1:
            maze[edit_point] = -maze[edit_point] + 1

        plt.clf()
        plot_maze(maze)

def edit_maze(maze, height, width):
    editable_points = np.array(list(itertools.product(range(1, height-1), range(1, width-1))))

    fig = plt.figure()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    plot_maze(maze)
    plt.show()

    return maze

if __name__ == "__main__":
    if len(sys.argv) == 1:
        while True:
            height = int(input("迷路の高さ >> "))
            width = int(input("迷路の幅 >> "))
            if height < 5 or width < 5 or height % 2 == 0 or width % 2 == 0:
                print("迷路の高さ・幅は5以上の奇数でなければなりません．")
                print()
                continue
            else:
                break
        maze = np.zeros((height, width), dtype=int)

        # 上下左右の壁を設定
        maze[ 0,  :] = 1
        maze[-1,  :] = 1
        maze[ :,  0] = 1
        maze[ :, -1] = 1

    else:
        maze = np.loadtxt(sys.argv[1], dtype=int)
        height, width = maze.shape

    maze = edit_maze(maze, height, width)
    if input("保存しますか?(y/n) >> ") == "y":
        name = input("迷路の名前(.txtを除く) >> ")

        plot_maze(maze, save_file=f"{name}.png")
        np.savetxt(f"{name}.txt", maze, fmt="%d")
        print(f"作成した迷路を{name}.pngと{name}.txtに保存しました．")
    print("処理を終了します．")
