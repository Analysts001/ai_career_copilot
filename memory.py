import json
import os

def save_memory(data, path="data/memory.json"):
    os.makedirs("data", exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f)

def load_memory(path="data/memory.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}