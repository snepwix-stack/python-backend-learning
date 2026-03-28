import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Tasks loaded")
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        logger.warning("File not found, returning empty")
        return {"tasks": []}


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump({"tasks": tasks}, f, ensure_ascii=False)
        logger.info("Task saved")
