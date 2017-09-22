#!/usr/local/bin/python3

graph_vertices = {}
graph_edges = {}

def add_node(node, g_v, g_e,*neighboures):
    neighbour_list = []
    edges_list = []
    for neighbour in neighboures:
        neighbour_list.append(neighbour)
        edges_list.append((node,neighbour))
        g_v[neighbour] = []
        g_e[neighbour] = []
    g_v[node] = neighbour_list
    g_e[node] = edges_list

def copy_node(node, g_v, g_e):
    current_vertices_list = g_v[node]
    current_edges_list = g_e[node]
    new_node = "{}-copy".format(node)
    new_vertices_list = []
    new_edges_list = []

    for vertice in current_vertices_list:
        new_vertice = "{}-copy".format(vertice)
        new_vertices_list.append(new_vertice)

    for edge in current_edges_list:
        node_one, node_two = edge
        new_node_one = "{}-copy".format(node_one)
        new_node_two = "{}-copy".format(node_two)
        new_edges_list.append((new_node_one, new_node_two))

    g_v[new_node] = new_vertices_list
    g_e[new_node] = new_edges_list

def find_path_to_from(to_node,current_node,g_v):

    vertices = g_v[current_node]
    print(current_node)
    if to_node in vertices:
        print("<-{}".format(from_node))
    else:
        for vertice in vertices:
            find_path_to_from(to_node, vertice, g_v)
    
    


def main():
    add_node('a',graph_vertices, graph_edges,'b','c','d')
    print(graph_vertices)
    print(graph_edges)
    copy_node('a',graph_vertices, graph_edges)
    print(graph_vertices)
    print(graph_edges)
    add_node('x',graph_vertices, graph_edges,'a')
    add_node('z',graph_vertices, graph_edges,'a')
    print(graph_vertices)
    print(graph_edges)
    print("Finding path to x from a:")
    find_path_to_from('x','a',graph_vertices)

if __name__ == "__main__" : main()
