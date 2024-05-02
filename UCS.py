graph_gn = {'A':[(4,'B'),(3,'C'),(7,'E')]
           ,'B':[(4,'A'),(6,'C'),(5,'D')]
           ,'C':[(3,'A'),(6,'B'),(11,'D'),(8,'E')]
           ,'D':[(5,'B'),(11,'C'),(2,'E'),(10,'G'),(2,'F')]
           ,'E':[(7,'A'),(8,'C'),(2,'D'),(5,'G')]
           ,'F':[(2,'D'),(3,'G')]
           ,'G':[(10,'D'),(5,'E'),(3,'F')]}

def ucs(graph, start, goal):
    explored = []
    import queue as pq
    q = pq.PriorityQueue()
    q.put((0,start))
    parents = {(0,start):None}
    while q:
        next_node = q.get()
        node = next_node[1]
        node_gn = next_node[0]
        if node not in explored:
            explored.append(node)
        else:
            continue
        if node == goal:
            path = [(node_gn,node)]
            prev_node = (node_gn,node)
            while prev_node != (0,start):
                parent = parents[prev_node]
                path.append(parent)
                prev_node = parent
            path.reverse()
            return path
        else:
            child = graph[node]
            child.sort()
            for (cost, nodes) in child:
                cost = node_gn + cost
                if (cost,nodes) not in parents:
                    parents[(cost,nodes)] = (node_gn,node)
                q.put((cost, nodes))

def print_path(path):
    for(cost,nodes) in path:
        print(nodes,end='  ')
def print_cost(path):
        print('\ncost : ',path[-1][0])

ucs_path = ucs(graph_gn,'A', 'F')

print('ucs : ',end='')
print_path(ucs_path)
print_cost(ucs_path)
