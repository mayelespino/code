#!/usr/local/bin/python3
from random import randint

graph = {}

def add_node(node, g, *edges):
    """
    :param node: the starting point
    :param g: The dictionary which contains it all.
    :param edges: Something like 'ab','bc'....
    :return: None
    """
    if node not in g:
        vertices = []
        existing_edges = []
    else:
        vertices, existing_edges = g[node]

    for edge in edges:
        if edge not in existing_edges:
            existing_edges.append(edge)

        point_a = edge[0]
        point_b = edge[1]

        if point_a not in vertices:
            vertices.append(point_a)
        if point_b not in vertices:
            vertices.append(point_b)

        if point_a not in g:
            point_a_edges = []
            point_a_vertices = []
            for edge in edges:
                if point_a in edge:
                    if edge not in point_a_edges:
                        point_a_edges.append(edge)
                    if edge[0] not in point_a_vertices:
                        point_a_vertices.append(edge[0])
                    if edge[1] not in point_a_vertices:
                        point_a_vertices.append(edge[1])
            g[point_a] = (point_a_vertices,point_a_edges)

        if point_b not in g:
            point_b_edges = []
            point_b_vertices = []
            for edge in edges:
                if point_b in edge:
                    point_b_edges.append(edge)
                    if edge[0] not in point_b_vertices:
                        point_b_vertices.append(edge[0])
                    if edge[1] not in point_b_vertices:
                        point_b_vertices.append(edge[1])
            g[point_b] = (point_b_vertices,point_b_edges)


    g[node] = (vertices, existing_edges)

def copy_node(node, g):
    original_edges, original_vertices = g[node]
    int_suffix = randint(0, 99)
    new_node = "{}-{}".format(node, int_suffix)
    existing_vertices, existing_edges = g[node]
    new_vertices = []
    new_edges = []

    for vertice in existing_vertices:
        new_vertices.append("{}-{}".format(vertice, int_suffix))
    for edge in existing_edges:
        new_edges.append("{}-{}".format(edge, int_suffix))

    g[new_node] = new_vertices, new_edges

def print_graph(g):
    for node in g:
        vertices, edges = graph[node]
        print("{0:<5}:\t{1}\n\t\t{2}".format(node, vertices, edges))

def recursive_search(to_node, current_node, g):
    vertecies, edges = g[current_node]

    if to_node in vertecies:
        print("{}=>{}".format(current_node, to_node))
        return 1

    for vertice in vertecies:
        if recursive_search(to_node, vertice, g) == 1:
            break
    return 0

def find_path_to_from(to_node,from_node,g):
    vertecies, edges = g[from_node]

    if to_node in vertecies:
        return 0

    print("starting from {}, looking for {}".format(from_node, to_node))
    for vertice in vertecies:
        print("{}->{}".format(from_node, vertice))
        if recursive_search(to_node, from_node, g) == 0:
            break

def main():
    add_node('a',graph, 'ab','ac','ad','bc','cd')
    add_node('a',graph, 'ax','ay')
    copy_node('a', graph)
    print_graph(graph)
    find_path_to_from('x', 'c', graph)
    find_path_to_from('y', 'b', graph)

if __name__ == "__main__" : main()