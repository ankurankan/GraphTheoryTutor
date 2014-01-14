import matplotlib
import networkx as nx
import json


def get_state(G):
    state = {'nodes': G.nodes(), 'edges': G.edges(), 'edge_color': {}, 'edge_line_width': {}, 'edge_line_style': {},
             'edge_alpha': {}, 'node_face_color': {}, 'node_edge_color': {}, 'node_size': {}, 'node_style': {},
             'node_alpha': {}}
    for node in G.nodes():
        for prop, value in G.node[node].items():
            state[prop][node] = value
    return state


def traverse_linked_list(linked_list):
    """
    Linked List in form of [(1,2), (2,3), (4,5), (5,6)]
    """
    trace = {}
    G = nx.DiGraph(linked_list)
    step = 0
    start = linked_list[0][0]
    G.node[start]['node_face_color'] = 'blue'
    trace[step] = get_state(G)
    step += 1
    end = linked_list[-1][-1]
    while start != end:
        start = G.neighbors(start)[0]
        G.node[start]['node_face_color'] = 'blue'
        trace[step] = get_state(G)
        step += 1
    print(json.dumps(trace))

if __name__ == '__main__':
    linked_list = [(1,2), (2,3), (3,4), (4,5), (5,6)]
    traverse_linked_list(linked_list)