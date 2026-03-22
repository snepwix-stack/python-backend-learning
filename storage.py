import json


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump({"tasks": tasks}, f, ensure_ascii=False)
