import json

def load_data():
    try:
        with open("stu.json", "r") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_data(students):
    with open("stu.json", "w") as f:
        json.dump(students, f, indent=2)