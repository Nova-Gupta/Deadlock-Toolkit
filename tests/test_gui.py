import pytest
import networkx as nx
from detection.detection import detect_deadlock
from prevention.bankers_algorithm import is_safe_state
from recovery.recovery import recover_from_deadlock

def test_deadlock_detection():
    """ Test the deadlock detection with parsed input from the GUI """
    processes = [1, 2, 3]
    allocations = [(1, 'R1'), ('R1', 2), (2, 'R2'), ('R2', 3), (3, 'R3'), ('R3', 1)]  # Complete cycle

    G = nx.DiGraph()
    G.add_edges_from(allocations)

    detected_cycle = detect_deadlock(G)
    print("Detected Cycle:", detected_cycle)  # Debugging output

    assert detected_cycle is not None, "Deadlock should be detected"


def test_prevention_safe_state():
    """ Test Banker's Algorithm for safe/unsafe states """
    available = [3, 3, 2]
    max_claim = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
    
    safe, sequence = is_safe_state(available, max_claim, allocation)
    
    assert not safe, "System should be in an unsafe state"

def test_recovery():
    """ Test deadlock recovery by terminating a process """
    processes = [1, 2]
    allocations = [(1, 'R1'), ('R1', 2), (2, 'R2'), ('R2', 1)]  # Deadlock

    G = nx.DiGraph()
    G.add_edges_from(allocations)

    process_priorities = {1: 1, 2: 2}  # Define process priorities
    updated_G, terminated_process = recover_from_deadlock(G, process_priorities)
    
    assert terminated_process in processes, "One of the processes should be terminated"

