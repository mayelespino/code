# dfs
# from: https://youtu.be/Urx87-NMm6c?si=-UD4yB5jyDJPchrK
#

from collections import deque

graph = {'a':['b','g'],
         'b': ['c','d','e'],
         'c': [],
         'd': [],
         'e':['f'],
         'f':[],
         'g':['h'],
         'h':['i'],
         'i':[],
        }

def dfs(graph, node):
    visited = []
    stack = deque()
    
    visited.append(node)
    stack.append(node)
    
    while stack:
        s = stack.pop()
        print(s, end="")
        
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

dfs(graph, 'a')