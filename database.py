import json
import os

FILE = "data.json"

default_data = {
    "total_queries": 0,
    "stats": {
        "admission": 0,
        "course": 0,
        "fee": 0,
        "internship": 0,
        "career": 0,
        "contact": 0
    }
}

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return default_data.copy()

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)