import networkx as nx

def create_test_graph():
    G = nx.DiGraph()
    G.add_edges_from([(1, 'R1'), ('R1', 2), (2, 'R2'), ('R2', 1)])
    return G
