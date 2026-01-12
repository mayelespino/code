graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
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

visited= []
visitNode('B')
print(visited)

visited= []
visitNode('C')
print(visited)

visited= []
visitNode('D')
print(visited)

visited= []
visitNode('E')
print(visited)

