def dijakstra(routes,  src, dest):
    
    parent_of = dict()
    cost_to = dict()
    visited = list()
    # initialize source
    parent_of[src] = src
    cost_to[src] = 0
    #n = len(routes)
    # first source is src
    x = find_route(routes, src, visited)
    
    while len(routes) >  len(visited) :
        # explore all the nodes reachable from x[0] if there any
        while x:
            visited.append(x)
            node, cost = routes[x][1], routes[x][2] 
            if not node in parent_of.keys():
                parent_of[node] = routes[x][0]
                cost_to [node] = cost + cost_to[routes[x][0]]
                x = find_route(routes, routes[x][0], visited)
                
            else:
                cum_cost = cost+cost_to[routes[x][0]]
                if cost_to[node] > cum_cost:
                    cost_to[node] = cum_cost
                    parent_of[node] = routes[x][0]
                    x = find_route(routes, routes[x][0], visited) 
             
            # find source for next iteration : find cost_to.keyMin
            nxt = [k for k, v in cost_to.items() if v == min(cost_to.values()) ]
            x = find_route(routes, nxt, visited)

        
    

def find_route(routes, x, visited):
     node = str()
     cost = 0
     for i in range(len(routes)):
         if not i in visited and  routes[i][0] == x :
             return i
     return False