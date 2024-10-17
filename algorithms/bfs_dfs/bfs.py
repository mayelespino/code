# bfs
# From: https://youtu.be/HZ5YTanv5QE?si=4YIKEl00RuGyBIhQ

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

def bfs(graph, node):
    visited = []
    queue = []
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end="")
        
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


bfs(graph, 'a')
