def BFS(graph,start,goal):
    visitedNodes = []
    queue = [start]
    while queue:
        node=queue.pop(0)
        if node in visitedNodes:
            continue
        else:
             visitedNodes.append(node)
        if node == goal:
           return visitedNodes
        else:
            neighbours = graph[node]
            for nodes in neighbours:
                queue.append(nodes)

graph = {'A':['B','D'],'B':['E'],'C':['A','G'],'D':['F'],'E':['C','G'],'F':['C','G'],'G':[]}

print('BFS : ',BFS(graph,'A','G'))


# bfs using queue class

import queue

def bfs(graph,start,goal):
       Queue = queue.Queue(maxsize=0)
       Queue.put(start)
       path = []
       while Queue:
           node = Queue.get()
           if node in path:
               continue
           else:
               path.append(node)
           if node == goal:
               return path
           for neighbour in graph[node]:
               Queue.put(neighbour)

print('bfs : ', bfs(graph,'A','G'))