import collections
from typing import List, Dict, Optional, Tuple

# --- 1. Define the Task Data Structure ---
class Task:
    """Represents a single task in the scheduling problem."""
    def __init__(self, name: str, duration: int, deadline: int, dependencies: List[str]):
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.dependencies = dependencies  # List of task names that must precede this task
        self.start_time: Optional[int] = None
        self.finish_time: Optional[int] = None
        
    def __repr__(self):
        """String representation for easy printing."""
        return (f"Task(name='{self.name}', duration={self.duration}, deadline={self.deadline}, "
                f"start={self.start_time}, finish={self.finish_time})")

# --- 2. The Heuristic Scheduling Algorithm ---
def schedule_tasks(tasks: List[Task]) -> Tuple[List[Task], int, int]:
    """
    Schedules tasks using a dependency-aware Earliest Deadline First (EDF) heuristic.
    
    Returns the scheduled tasks, the total makespan, and the total tardiness.
    """
    
    # Map task names to Task objects for easy lookup
    task_map: Dict[str, Task] = {t.name: t for t in tasks}
    
    # 2.1. Determine Precedence Counts (In-degrees) for Topological Sort
    # The in_degree is the number of predecessors a task has that are NOT yet finished.
    in_degree: Dict[str, int] = {t.name: len(t.dependencies) for t in tasks}
    
    # 2.2. Initialize the set of tasks that are READY to be scheduled
    # A task is ready if its in-degree is 0 (all dependencies are met).
    ready_queue: List[Task] = sorted(
        [t for t in tasks if in_degree[t.name] == 0],
        key=lambda t: t.deadline  # Sort by Earliest Deadline First (EDF)
    )
    
    current_time = 0
    scheduled_tasks: List[Task] = []
    
    # Create an adjacency list (task -> list of its successors) for dependency updates
    successors: Dict[str, List[str]] = collections.defaultdict(list)
    for task in tasks:
        for dependency_name in task.dependencies:
            successors[dependency_name].append(task.name)

    # 2.3. Main Scheduling Loop
    while ready_queue:
        # Get the highest priority task (Earliest Deadline First)
        current_task = ready_queue.pop(0)
        
        # Schedule the task: Start time is the current time
        current_task.start_time = current_time
        current_task.finish_time = current_time + current_task.duration
        
        # Update the project time
        current_time = current_task.finish_time
        scheduled_tasks.append(current_task)
        
        # 2.4. Update Dependencies (Successor In-degrees)
        # For every task that depended on the *current_task*:
        for successor_name in successors[current_task.name]:
            # Decrease its in-degree
            in_degree[successor_name] -= 1
            
            # If the successor's in-degree is now 0, it is ready
            if in_degree[successor_name] == 0:
                successor_task = task_map[successor_name]
                ready_queue.append(successor_task)
        
        # Re-sort the ready queue by EDF after adding new ready tasks
        ready_queue.sort(key=lambda t: t.deadline)

    # 3. Calculate Metrics
    
    # Makespan: The total time required to complete all tasks
    makespan = current_time 
    
    # Total Tardiness: Sum of (Finish Time - Deadline) for all late tasks
    total_tardiness = 0
    for task in scheduled_tasks:
        if task.finish_time is not None and task.finish_time > task.deadline:
            total_tardiness += task.finish_time - task.deadline
            
    return scheduled_tasks, makespan, total_tardiness

# --- 3. Example Usage ---
if __name__ == '__main__':
    
    # Example Task Set (Units can be days, hours, etc.)
    # Tasks: A -> B, A -> C, B -> D, C -> D, E (independent)
    tasks_data = [
        Task('A', duration=3, deadline=10, dependencies=[]),
        Task('B', duration=2, deadline=8, dependencies=['A']),
        Task('C', duration=4, deadline=12, dependencies=['A']), # C is longer but has a later deadline
        Task('D', duration=1, deadline=11, dependencies=['B', 'C']),
        Task('E', duration=5, deadline=7, dependencies=[]), # Task E is independent and critical
    ]

    # --- Run the Scheduler ---
    scheduled_tasks, makespan, total_tardiness = schedule_tasks(tasks_data)

    # --- Output Results ---
    print("## ✅ Scheduled Tasks (EDF Heuristic) ##")
    for task in scheduled_tasks:
        print(f"  - {task.name}: Start={task.start_time}, Finish={task.finish_time}, Deadline={task.deadline}")
        tardiness = max(0, task.finish_time - task.deadline if task.finish_time is not None else 0)
        if tardiness > 0:
            print(f"    * LATE by {tardiness}")

    print("\n--- Summary Metrics ---")
    print(f"**Total Makespan (Project Completion Time):** {makespan}") #
    print(f"**Total Tardiness:** {total_tardiness}") #

    # ```

### Key Heuristic Logic
