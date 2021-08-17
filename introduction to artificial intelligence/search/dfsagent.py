from aisearchtools import *
    
p_mat = [
        [13, 12, 11,'X','X',  2,  1,  0],
        ['X',11, 10,  9,'X',  3,'X',  1],
        [15,'X','X',  8,'X',  4,  3,  2],
        [14, 15,'X',  7,  6,  5,  4,  3],
        [13,'X',  9,  8,  7,  6,'X',  4],
        [12, 11,'X',  9,'X',  7,  6,  5],
        ['X',12, 11, 10, 11,'X','X','X']
        
    ]


def conv(prb):
    r = len(prb)
    c = len(prb[0])
    a = [[0 if type(prb[i][j]) is int else 1 for j in range(c)] for  i in range(r)]
    return a
    #for i in range():
     #   for j in range():
      #      if prb[i,j]

#prb = conv(p_mat) 
#Problem.view_matrix(prb)
#state_space = Problem.to_statespace(prb)
#Problem.view_graph(state_space)


# test 2 easy
nodes = [Node(i) for i in 'A B C D E F'.split()]
nodes[0].actions = [1, ]
nodes[1].actions = [2,3]
nodes[2].actions = [4,]
nodes[3].actions = [5,]

Problem.view_graph(nodes)
agent = DfsAgent(nodes, 0, 4)
agent.explore()
print(agent.path)
print(agent.memo)
