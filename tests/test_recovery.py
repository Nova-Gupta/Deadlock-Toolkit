import sys
import os
import networkx as nx
import pytest

# Add project root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from recovery.recovery import recover_from_deadlock

def test_no_deadlock():
    """ Test case: No deadlock scenario """
    G = nx.DiGraph()
    G.add_edges_from([(1, 'R1'), ('R1', 2), (2, 'R2')])  # No cycle (no deadlock)
    
    updated_G, terminated_process = recover_from_deadlock(G)
    assert updated_G is None and terminated_process is None  # No recovery needed

def test_deadlock_recovery():
    """ Test case: Deadlock recovery scenario """
    G = nx.DiGraph()
    G.add_edges_from([(1, 'R1'), ('R1', 2), (2, 'R2'), ('R2', 1)])  # Cycle present

    updated_G, terminated_process = recover_from_deadlock(G, process_priorities={1: 1, 2: 2})
    
    assert terminated_process == 2  # Process 2 has lower priority (higher value)
    assert 2 not in updated_G.nodes  # Ensure process 2 is removed

def test_deadlock_recovery_equal_priority():
    """ Test case: Deadlock recovery scenario where all processes have equal priority """
    G = nx.DiGraph()
    G.add_edges_from([(1, 'R1'), ('R1', 2), (2, 'R2'), ('R2', 1)])  # Cycle present

    updated_G, terminated_process = recover_from_deadlock(G)
    
    assert terminated_process in {1, 2}  # Any process can be terminated
    assert terminated_process not in updated_G.nodes  # Ensure removal
