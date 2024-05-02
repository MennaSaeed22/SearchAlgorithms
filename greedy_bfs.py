graph_hn = {'A':[(30,'B'),(44,'E'),(56,'C')]
            ,'B':[(28,'A'),(56,'C'),(60,'D')]
            ,'C':[(28,'A'),(30,'B'),(44,'E'),(60,'D')]
            ,'D':[(0,'F'),(30,'B'),(36,'G'),(44,'E'),(56,'C')]
            ,'E':[(28,'A'),(36,'G'),(56,'C'),(60,'D')]
            ,'F':[(36,'G'),(60,'D')]
            ,'G':[(0,'F'),(44,'E'),(60,'D')]}

def greedy_bfs(graph,start,goal,explored=[]):
    while goal not in explored:
        import queue as pq
        q = pq.PriorityQueue()
        if start not in explored:
            explored.append(start)
        child = graph[start]
        for (h,node) in child:
            if node not in explored:
                q.put((h,node))
        new = q.get()
        greedy_bfs(graph,new[1],goal,explored)
        return explored

def print_greedy(path):
    for i in range(len(path)):
        print(path[i],end='  ')

print('greedy : ',end='')
print_greedy(greedy_bfs(graph_hn,'A','F'))