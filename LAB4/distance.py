import sys
import math

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if len(sys.argv) != 5:
    print("Usage: python distance.py x1 y1 x2 y2")
    sys.exit(1)

try:
    x1, y1, x2, y2 = map(float, sys.argv[1:])
except ValueError:
    print("Please enter valid numbers for coordinates.")
    sys.exit(1)

man_dist = manhattan_distance(x1, y1, x2, y2)
euc_dist = euclidean_distance(x1, y1, x2, y2)

print(f"Manhattan distance between points: {man_dist}")
print(f"Euclidean distance between points: {euc_dist}")
