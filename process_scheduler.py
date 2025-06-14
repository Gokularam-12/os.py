def run_fcfs():
    processes = [("P1", 5), ("P2", 3), ("P3", 8)]
    time = 0
    print("\n--- FCFS Scheduling ---")
    for pid, bt in processes:
        print(f"{pid} starts at {time}, ends at {time + bt}")
        time += bt

def run_sjf():
    processes = [("P1", 5), ("P2", 3), ("P3", 8)]
    print("\n--- SJF Scheduling ---")
    sorted_procs = sorted(processes, key=lambda x: x[1])
    time = 0
    for pid, bt in sorted_procs:
        print(f"{pid} starts at {time}, ends at {time + bt}")
        time += bt

def run_rr():
    processes = [("P1", 5), ("P2", 3), ("P3", 8)]
    quantum = 2
    print("\n--- Round Robin Scheduling ---")
    queue = processes[:]
    time = 0
    while any(bt > 0 for _, bt in queue):
        for i in range(len(queue)):
            pid, bt = queue[i]
            if bt > 0:
                exec_time = min(quantum, bt)
                print(f"{pid} runs from {time} to {time + exec_time}")
                queue[i] = (pid, bt - exec_time)
                time += exec_time
