from maze import Maze
import sys

try:
    maze = Maze(int(sys.argv[1])) # Uses command line argument to generate maze with given size
    maze.generate_maze()
    maze.print()
    print("Welcome to 2D maze")
except:
    print("Exception Occurred. Maze size not given or incorrect format.")
