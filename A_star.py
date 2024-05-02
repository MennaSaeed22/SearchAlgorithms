graph_gn = {'S':[(2,'A'),(5,'D')]
            ,'A':[(1,'B'),(2,'D'),(2,'S')]
            ,'B':[(1,'A'),(4,'C'),(5,'E')]
            ,'C':[(4,'B')]
            ,'D':[(2,'A'),(2,'E'),(2,'S')]
            ,'E':[(2,'D'),(4,'F'),(5,'B')]
            ,'F':[(3,'G'),(4,'E')]}

h_value = {'S':11.0
            ,'A':10.4
            ,'B':6.7
            ,'C':4.0
            ,'D':8.4
            ,'E':6.9
            ,'F':3.0
            ,'G':0}

def A_star(graph_g,h,start,goal):
    explored = []
    import queue as pq
    q = pq.PriorityQueue()
    q.put((h[start],start))
    parents = {(h[start],start): None}
    while q:
        next_node = q.get()
        node = next_node[1]
        if node == start:
            node_fn = h[start]
        else:
            node_fn = next_node[0]
        if node not in explored:
            explored.append(node)
        else:
            continue
        if node == goal:
            path = [(node_fn,node)]
            prev_node = (node_fn,node)
            while prev_node != (h[start],start):
                parent = parents[prev_node]
                path.append(parent)
                prev_node = parent
            path.reverse()
            return path
        else:
            child_g = graph_g[node]
            for (cost, nodes) in child_g:
                fn = (node_fn-h[node]) + cost + h[nodes]
                if (fn,nodes) not in parents:
                    parents[(fn,nodes)] = (node_fn,node)
                q.put((fn,nodes))
def print_path(path):
    for(cost,nodes) in path:
        print(nodes,end='  ')
def print_cost(path):
        print('\ncost : ',path[-1][0])

print('A* : ',end='')
print_path(A_star(graph_gn,h_value,'S', 'G'))
print_cost(A_star(graph_gn,h_value,'S', 'G'))
