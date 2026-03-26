import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
ASSETS_DIR = PROJECT_ROOT / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"

LOGS_DIR = PROJECT_ROOT / "logs"