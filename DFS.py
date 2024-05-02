#  dfs using recursion

def DFS(graph,start,goal,visitedNodes=[]):
    while goal not in visitedNodes:
         node = start
         if node not in visitedNodes:
            visitedNodes.append(node)
            for neighbour in graph[node]:
               DFS(graph, neighbour,goal,visitedNodes)
         return visitedNodes

graph = {'A':['B','D'],'B':['E'],'C':['A','G'],'D':['F'],'E':['C','G'],'F':['C','G'],'G':[]}

print('DFS : ', DFS(graph,'A','G'))

# DFS using stack

from queue import LifoQueue

def dfs(graph,start,goal):
    stack = LifoQueue(maxsize=0)
    stack.put(start)
    path = []
    while stack:
        node = stack.get()
        if node in path:
            continue
        else:
           path.append(node)
        if node == goal:
            return path
        for neighbour in graph[node]:
           stack.put(neighbour)

graph = {'A':['D','B'],'B':['E'],'C':['G','A'],'D':['F'],'E':['G','C'],'F':['G','C'],'G':[]}

print('dfs : ',dfs(graph,'A','G'))