import networkx as nx

def detect_deadlock(graph):
    """
    Detects deadlock in a given directed graph using cycle detection.
    
    Parameters:
        graph (networkx.DiGraph): A directed graph representing process-resource allocation.

    Returns:
        list: A list of nodes forming a cycle (deadlock) or None if no deadlock exists.
    """
    try:
        cycle = nx.find_cycle(graph, orientation="original")  # Detects cycles (deadlock)
        return cycle  # Returns the cycle causing deadlock
    except:
        return None  # No deadlock found
