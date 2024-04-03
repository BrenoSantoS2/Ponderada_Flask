from tinydb import TinyDB
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class logs:
    robot_action: str
    date: str
    time: str

db = TinyDB(Path(__file__).parent.parent/ "Database" / "db.json")

def get_logs():
    return db.all()

