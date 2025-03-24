
from prevention.bankers_algorithm import is_safe_state

def test_safe_state():
    available = [3, 3, 2]
    max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    safe, sequence = is_safe_state(available, max_demand, allocation)
    assert safe is True
    assert len(sequence) == len(max_demand)

def test_unsafe_state():
    available = [1, 1, 0]
    max_demand = [[2, 2, 2], [1, 1, 1]]
    allocation = [[1, 0, 0], [0, 1, 1]]
    safe, sequence = is_safe_state(available, max_demand, allocation)
    assert safe is False
    assert sequence == []
