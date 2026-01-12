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

def visitNode(node):
    if node in visited:
        return
    visited.append(node)

    for currentNode in graph[node]:
        visitNode(currentNode)


visitNode('A')
print(visited)

