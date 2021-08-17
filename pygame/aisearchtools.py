class Node:
""" 
Base Node class: every states of actual problem to be converted into
this datastructure. A node representes each point in the problem set
"""
    def __init__(self, state+None, action+None, cost+None):
        self.state = state
        self.action = action
        self.parent = parent
        self.cost = cost
    
    def __eq__(self, other):
        return self.state == other.state

class Agent:
"""
Base Artificial Agent Class thst percieves a given envioronment and acts upon
# defalut container is list
"""
    def __init__(self, start_state, end_state, container= list()):
        self.memo = set()
        self.container = container
        self.state = start_state
        self.goal = end_state

    # override
    def action(self):
"""while nodes in self.state.action.pop: self.container
"""
        pass

    # override
    def transition(self):
        pass

    # Only to run unless you cetainly know what wre you doing
    def explore(self):
        if self.state == self.goal:
            return self.state

        self.action()
        self.transition()
        return self.explore() if self.container else False
 
 
 class dfsAgent(Agent):
    def __init__(self, state_space, start, end):
        super.__init__(self,start, end):
        
        self.path = list()
        self.cost = int()

# utility function that converts a (sparce)mattrix to Graph 
def state_space(problem, row, col):
    """
    Converts a problem matrix to a Graph G(State Space)
    """
    state_space = list()
    # make nodes
    for i in range(row): # row
        for j in range(col): #column
            actions = set()
            # if visitable
            if not problem[i][j]:
                #find neighbours
                #left
                if (j-1) >= 0 and not problem[i][j-1]:
                    actions.add((i, j-1))
                #right
                if (j+1) < col and not problem[i][j+1]:
                    actions.add((i, j+1))
                #up
                if (i-1) >= 0 and not problem[i-1][j]:
                    actions.add((i-1, j))
                #down
                if (i+1) < row and not problem[i+1][j]:
                    actions.add((i+1, j))
                
                # create node
                state_space.append(Node((i, j), actions))
    return state_space
# utility function to print mattrix as 2d
def pp(a, row, col):
    print('\t')
    for _,j in enumerate(a):
        print(*j)

# sample Problem 

prb = [
    [1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0 ,1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1]
]
row = len(prb)
col = len(prb[0])

pp(state_space(prb, row, col))
