from maze import Maze
import sys

try:
    maze_size = int(sys.argv[1])
    maze = Maze(maze_size)
    maze.generate_maze()
    maze.print()
    print("Welcome to 2D maze")
except:
    print("Exception Occurred. Maze size not given or incorrect format.")
