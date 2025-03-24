def is_safe_state(available, max_demand, allocation):
    """
    Implements the Banker's Algorithm to check for a safe state.
    
    :param available: List of available resources.
    :param max_demand: Matrix of maximum demand of each process.
    :param allocation: Matrix of allocated resources to each process.
    :return: (safe, sequence) where safe is True if system is in a safe state, and sequence is the safe sequence.
    """
    import copy
    
    num_processes = len(max_demand)
    num_resources = len(available)
    
    work = copy.deepcopy(available)
    finish = [False] * num_processes
    safe_sequence = []
    
    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                need = [max_demand[i][j] - allocation[i][j] for j in range(num_resources)]
                if all(need[j] <= work[j] for j in range(num_resources)):
                    safe_sequence.append(i)
                    work = [work[j] + allocation[i][j] for j in range(num_resources)]
                    finish[i] = True
                    found = True
                    break
        if not found:
            return False, []  # No safe sequence found
    
    return True, safe_sequence
