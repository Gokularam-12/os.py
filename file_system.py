vfs = {
    "/": ["file1.txt", "dir1"],
    "/dir1": ["file2.txt"]
}

def list_dir(path):
    return vfs.get(path, ["[Empty or Invalid Directory]"])

def make_dir(path, name):
    new_path = f"{path}/{name}" if path != "/" else f"/{name}"
    if new_path not in vfs:
        vfs[new_path] = []
        vfs[path].append(name)
        print(f"Directory '{name}' created under {path}")
    else:
        print("Directory already exists.")
