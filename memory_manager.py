def simulate_memory():
    blocks = [100, 500, 200, 300, 600]
    process_size = 250

    print("\n--- First Fit Allocation ---")
    for i, b in enumerate(blocks):
        if b >= process_size:
            print(f"Allocated to block {i + 1} of size {b}")
            break

    print("\n--- Best Fit Allocation ---")
    best = min((b for b in blocks if b >= process_size), default=None)
    if best:
        print(f"Allocated to best block of size {best}")

    print("\n--- Worst Fit Allocation ---")
    worst = max((b for b in blocks if b >= process_size), default=None)
    if worst:
        print(f"Allocated to worst block of size {worst}")
