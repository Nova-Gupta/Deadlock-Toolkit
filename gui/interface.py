import tkinter as tk
from tkinter import messagebox
import networkx as nx
from detection.detection import detect_deadlock
from prevention.bankers_algorithm import is_safe_state
from recovery.recovery import recover_from_deadlock

class DeadlockToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Toolkit")
        self.root.geometry("600x400")

        # Title Label
        self.label_title = tk.Label(root, text="Deadlock Toolkit", font=("Arial", 16, "bold"))
        self.label_title.pack(pady=10)

        # Input Fields
        self.label_processes = tk.Label(root, text="Processes (comma-separated):")
        self.label_processes.pack()
        self.entry_processes = tk.Entry(root)
        self.entry_processes.pack()

        self.label_resources = tk.Label(root, text="Resources (comma-separated):")
        self.label_resources.pack()
        self.entry_resources = tk.Entry(root)
        self.entry_resources.pack()

        self.label_allocations = tk.Label(root, text="Allocations (comma-separated, row-wise):")
        self.label_allocations.pack()
        self.entry_allocations = tk.Entry(root)
        self.entry_allocations.pack()

        # Buttons
        self.btn_detect = tk.Button(root, text="Run Deadlock Detection", command=self.run_deadlock_detection, bg="red", fg="white")
        self.btn_detect.pack(pady=5)

        self.btn_prevent = tk.Button(root, text="Run Deadlock Prevention (Banker's Algorithm)", command=self.run_deadlock_prevention, bg="blue", fg="white")
        self.btn_prevent.pack(pady=5)

        self.btn_recover = tk.Button(root, text="Run Deadlock Recovery", command=self.run_deadlock_recovery, bg="green", fg="white")
        self.btn_recover.pack(pady=5)

    def parse_allocations(self):
        """Parse allocations from comma-separated values into a matrix."""
        try:
            processes = self.entry_processes.get().split(",")
            resources = self.entry_resources.get().split(",")

            num_processes = len(processes)
            num_resources = len(resources)

            values = list(map(int, self.entry_allocations.get().split(",")))  

            if len(values) != num_processes * num_resources:
                raise ValueError("Incorrect number of allocation values.")

            return [values[i * num_resources:(i + 1) * num_resources] for i in range(num_processes)]
        except ValueError:
            messagebox.showerror("Error", "Invalid Input: Ensure proper numeric values separated by commas.")
            return None

    def run_deadlock_detection(self):
        try:
            allocations = self.parse_allocations()
            if allocations is None:
                return  # Exit if parsing fails

            G = nx.DiGraph()
            for i, row in enumerate(allocations):
                for j, alloc in enumerate(row):
                    if alloc > 0:
                        G.add_edge(f"P{i}", f"R{j}")

            if detect_deadlock(G):
                messagebox.showwarning("Deadlock Detection", "Deadlock detected in the system!")
            else:
                messagebox.showinfo("Deadlock Detection", "No deadlock detected.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")

    def run_deadlock_prevention(self):
        try:
            available = list(map(int, self.entry_resources.get().split(",")))
            allocation = self.parse_allocations()
            max_claim = self.parse_allocations()  

            if allocation is None or max_claim is None:
                return  

            safe, sequence = is_safe_state(available, max_claim, allocation)
            if safe:
                messagebox.showinfo("Deadlock Prevention", f"System is in a safe state. Safe sequence: {sequence}")
            else:
                messagebox.showwarning("Deadlock Prevention", "System is in an unsafe state!")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")

    def run_deadlock_recovery(self):
        try:
            allocations = self.parse_allocations()
            if allocations is None:
                return  

            G = nx.DiGraph()
            for i, row in enumerate(allocations):
                for j, alloc in enumerate(row):
                    if alloc > 0:
                        G.add_edge(f"P{i}", f"R{j}")

            updated_G, terminated_process = recover_from_deadlock(G)
            if terminated_process is not None:
                messagebox.showinfo("Deadlock Recovery", f"Deadlock resolved by terminating process: {terminated_process}")
            else:
                messagebox.showwarning("Deadlock Recovery", "No deadlock detected, no process terminated.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlockToolkitGUI(root)
    root.mainloop()
