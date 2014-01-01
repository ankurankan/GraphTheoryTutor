import matplotlib
import nx_animation as nx_anim

matplotlib.use('Agg')
import matplotlib.pyplot as plt

__author__ = 'Ankur Ankan'

step = 0
trace = {}


def get_state(G):
    state = {'nodes': G.nodes(), 'edges': G.edges(), 'edge_color': {}, 'edge_line_width': {}, 'edge_line_style': {},
             'edge_alpha': {}, 'node_face_color': {}, 'node_edge_color': {}, 'node_size': {}, 'node_style': {},
             'node_alpha': {}}

    # TODO: Add a check if graph has already been plotted
    # Considering that graph has been plotted
    axes = plt.gca()
    number_of_nodes = G.number_of_nodes()

    node_collection = axes.get_children()[number_of_nodes + 2]
    node_face_color = node_collection.get_facecolor().tolist()
    if len(node_face_color) == 1:
        for node in G.nodes():
            state['node_face_color'][node] = node_face_color[0]
    else:
        for i in range(number_of_nodes):
            state['node_face_color'][G.nodes[i]] = node_face_color[i]

    return state


def neighbours(G, color):
    neighbours = G.neighbours()
    for node in neighbours:
        nx_anim.set_node_facecolor(G, node=node, color=color)
    trace[step] = get_state(G)
    step += 1
