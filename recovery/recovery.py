import networkx as nx

def recover_from_deadlock(G, process_priorities=None):
    """
    Detects and resolves deadlocks by removing the lowest priority process from the cycle.

    :param G: Directed graph representing resource allocation (DiGraph)
    :param process_priorities: Dictionary mapping processes to priority levels (lower value = higher priority)
    :return: Tuple (updated graph, terminated process) or (None, None) if no deadlock detected
    """
    try:
        cycle_edges = nx.find_cycle(G, orientation='original')
        cycle_nodes = set(node for edge in cycle_edges for node in edge)  # Extract nodes involved in the cycle
        processes = {node for node in cycle_nodes if isinstance(node, int)}  # Only process nodes

        if not processes:
            return None, None  # No process in the cycle (shouldn't happen, but safety check)

        if not process_priorities:
            process_priorities = {p: float('inf') for p in processes}  # Default: all processes equal priority

        # Identify the process with the lowest priority (higher value means lower priority)
        process_to_terminate = max(processes, key=lambda p: process_priorities.get(p, float('inf')))

        # Remove the selected process from the graph
        G.remove_node(process_to_terminate)

        return G, process_to_terminate

    except nx.NetworkXNoCycle:
        return None, None  # No deadlock detected
