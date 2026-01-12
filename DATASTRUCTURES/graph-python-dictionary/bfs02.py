graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': ['I'],
    'I': []
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
        bfs.append(currentNode)
    for currentNode in bfs:
        visitNode(currentNode)

visitNode('A')
print(visited)
