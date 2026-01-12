graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

visited = []
bfs = []

def visitNode(node):
    if node in visited:
        return

    visited.append(node)
    bfs.append(node)
    for currentNode in graph[node]:
        if currentNode in visited:
            continue
        visitNode(currentNode)


visitNode('A')
print(bfs)

bfs = []
visited = []
visitNode('B')
print(bfs)

bfs = []
visited = []
visitNode('C')
print(bfs)

bfs = []
visited = []
visitNode('D')
print(bfs)

bfs = []
visited = []
visitNode('E')
print(bfs)
