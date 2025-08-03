import os
import json
from datetime import datetime

def save_memory(payload_data, path="logs/memory_seed.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    memory_entry = {
        "timestamp": datetime.now().isoformat(),
        "memory": payload_data
    }

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(memory_entry)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
