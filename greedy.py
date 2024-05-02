graph_hn = {'A':[(30,'B'),(44,'E'),(56,'C')]
           ,'B':[(28,'A'),(56,'C'),(60,'D')]
           ,'C':[(28,'A'),(30,'B'),(44,'E'),(60,'D')]
           ,'D':[(0,'F'),(30,'B'),(36,'G'),(44,'E'),(56,'C')]
           ,'E':[(28,'A'),(36,'G'),(56,'C'),(60,'D')]
           ,'F':[(36,'G'),(60,'D')]
           ,'G':[(0,'F'),(44,'E'),(60,'D')]}

def greedy(graph,start,goal):
    explored = []
    import queue as pq
    q = pq.PriorityQueue()
    q.put((0,start))
    parents = {(0,start):None}
    while q:
        next_node = q.get()
        node = next_node[1]
        node_hn = next_node[0]
        if node not in explored:
            explored.append(node)
        else:
            continue
        if node == goal:
            path = [(node_hn,node)]
            prev_node = (node_hn,node)
            while prev_node != (0,start):
                parent = parents[prev_node]
                path.append(parent)
                prev_node = parent
            path.reverse()
            return path
        else:
            child = graph[node]
            child.sort()
            for (h, nodes) in child:
                if (h,nodes) not in parents:
                    parents[(h,nodes)] = (node_hn,node)
                q.put((h, nodes))

def print_path(path):
    for(cost,nodes) in path:
        print(nodes,end='  ')

print('greedy : ',end='')
print_path(greedy(graph_hn,'A','F'))
