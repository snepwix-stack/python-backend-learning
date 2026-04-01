from dataclasses import dataclass


@dataclass
class Task:
    text: str
    priority: str
    id: int
    done: bool = False

    def __str__(self):
        status = "✅" if self.done else "❌"
        return f"[{self.id}] {self.text} | {self.priority} | {status}"
