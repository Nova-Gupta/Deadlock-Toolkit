import sys
import os

# Add project root directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import networkx as nx
from detection.detection import detect_deadlock  # Correct import

def test_no_deadlock():
    """ Test case: No deadlock scenario """
    G = nx.DiGraph()
    G.add_edges_from([(1, 'R1'), ('R1', 2), (2, 'R2')])  # No cycle (no deadlock)
    assert detect_deadlock(G) is None

def test_deadlock_detected():
    """ Test case: Deadlock scenario """
    G = nx.DiGraph()
    G.add_edges_from([(1, 'R1'), ('R1', 2), (2, 'R2'), ('R2', 1)])  # Cycle present
    assert detect_deadlock(G) is not None
