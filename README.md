# Deadlock Toolkit

## Overview
The Deadlock Toolkit is a Python-based application that helps users detect, prevent, and recover from deadlocks in process-resource allocation scenarios. The GUI is built using Tkinter and leverages NetworkX for graph-based deadlock detection.

## Features
- **Deadlock Detection**: Identifies cycles in a process-resource allocation graph.
- **Deadlock Prevention**: Uses the Banker's Algorithm to determine safe states.
- **Deadlock Recovery**: Resolves deadlocks by terminating processes based on priority.

## Installation

### Prerequisites
- Python 3.12 or later
- Required dependencies (listed in `requirements.txt`)

### Steps
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/nova-gupta/Deadlock-Toolkit.git
   cd Deadlock-Toolkit

```sh
pip install -r requirements.txt
```

## Running the GUI

To launch the Deadlock Toolkit GUI, run:

```sh
python main.py
```

## Example Test Case

Use the following values in the GUI to test its functionality:

### Inputs:
- **Processes**: `1,2,3`
- **Resources**: `3,3,2`
- **Allocations**: `0,1,0,2,0,0,3,0,2`

### Expected Behavior:
- **Detection**: Should identify a deadlock if a cycle exists in the process-resource graph.
- **Prevention**: Should determine if the system is in a safe or unsafe state.
- **Recovery**: Should suggest a process termination to resolve deadlock.

## Running Tests

To validate the implementation, run:

```sh
pytest
```

This will execute unit tests for detection, prevention, and recovery mechanisms.

## Project Structure
```
Deadlock-Toolkit/
│── detection/
│   ├── detection.py
│── prevention/
│   ├── bankers_algorithm.py
│── recovery/
│   ├── recovery.py
│── gui/
│   ├── interface.py
│── tests/
│   ├── test_detection.py
│   ├── test_prevention.py
│   ├── test_recovery.py
│── main.py
│── README.md
│── requirements.txt
```

## Contributors

- @nova-gupta
- @Ankureet

## License
This project is licensed under the MIT License.

