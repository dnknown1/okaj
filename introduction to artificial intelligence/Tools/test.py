from aiUtils.searchTools import *
from sys import argv
from pprint import pprint as pp


problem_matrix = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 1, 0]
]
start = (0, 0)
goal = (3, 1)
container = Aqueue() if len(argv) > 1 else Astack()
cost_func = lambda x: 1

location, graph = solve(problem_matrix, start, goal, cost_func, container)

pp(track_path(graph, location.state))