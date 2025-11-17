import json, os

path = os.path.join(os.path.dirname(__file__), "..", "data", "notes.json")

def add_note(text):
    with open(path, "r+") as f:
        data = json.load(f)
        data["notes"].append(text)
        f.seek(0)
        json.dump(data, f, indent=4)

def get_notes():
    with open(path) as f:
        data = json.load(f)
    return data["notes"]
