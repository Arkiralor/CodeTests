from os import path
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent
DATA_DIR: Path = path.join(BASE_DIR, "data")
SCRIPTS_DIR: Path = path.join(BASE_DIR, "scripts")