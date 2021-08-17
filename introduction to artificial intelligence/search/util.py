class Node():
    def __init__(self, state+None, parent=None, action=None, cost= None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# AI Search Agent
class Agent:
    
    def __init__(self, state_space=Object(), initial_state=Object(), terminal_state=Object()):
        # entire problem 
        self.state_space = state_space
        # initial state
        self.loc = Node()
        # terminal state
        self.goal = terminal_state
        # underlying date structure (to be used in base class)
        self.container = Object()
        # memoization
        self.memo = Object()
        # cumulative cost
        self.cost = object()

    # ***Overide: Transition Model
    def transition(self):
        pass

    # ***Override: call to Solve the Problem
    def solve(self):
        pass
