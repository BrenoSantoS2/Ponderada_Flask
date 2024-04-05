from tinydb import TinyDB
from dataclasses import dataclass, asdict
import datetime
from pathlib import Path

@dataclass
class logs:
    robot_action: str
    date: str
    time: str

db = TinyDB(Path(__file__).parent.parent/ "Database" / "db.json")

def get_logs():
    return db.all()

def insert_log(robot_action):
    time = datetime.datetime.now()
    log = logs(robot_action, time.strftime("%d/%m/%Y"), time.strftime("%H:%M:%S"))
    db.insert(asdict(log))
    

