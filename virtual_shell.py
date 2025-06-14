from process_scheduler import *
from memory_manager import *
from file_system import *

current_path = "/"

def start_shell():
    global current_path
    while True:
        cmd = input(f"VirtualOS:{current_path}$ ").strip()
        if cmd == "exit":
            break
        elif cmd == "help":
            print("Commands: ls, cd <dir>, mkdir <dir>, fcfs, sjf, rr, memory, exit")
        elif cmd == "ls":
            print(list_dir(current_path))
        elif cmd.startswith("cd "):
            path = cmd.split()[1]
            if path == "..":
                current_path = "/" if current_path == "/" else "/".join(current_path.rstrip("/").split("/")[:-1])
            else:
                current_path += f"/{path}" if current_path != "/" else f"{path}"
        elif cmd.startswith("mkdir "):
            name = cmd.split()[1]
            make_dir(current_path, name)
        elif cmd == "fcfs":
            run_fcfs()
        elif cmd == "sjf":
            run_sjf()
        elif cmd == "rr":
            run_rr()
        elif cmd == "memory":
            simulate_memory()
        else:
            print("Command not found. Try 'help'")

