import logging
import json
from dataclasses import asdict
from models import Task

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Tasks loaded")
            return [Task(**t) for t in data["tasks"]]
    except (FileNotFoundError, json.JSONDecodeError):
        logger.warning("File not found, returning empty")
        return []


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump({"tasks": [asdict(t) for t in tasks]}, f, ensure_ascii=False)
        logger.info("Task saved")
