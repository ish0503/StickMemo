import os
import sys
import json


def app_data_root():
    # Windows AppData 사용 (배포 정석)
    base = os.getenv("LOCALAPPDATA")

    if not base:
        base = os.path.expanduser("~")

    path = os.path.join(base, "StickyNotes")
    return path


DATA_DIR = os.path.join(app_data_root(), "data")
FILE = os.path.join(DATA_DIR, "notes.json")


class Storage:

    @staticmethod
    def load():
        try:
            if not os.path.exists(FILE):
                return []

            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except:
            # JSON 깨졌을 때 앱 안 죽게
            return []

    @staticmethod
    def save(data):
        os.makedirs(DATA_DIR, exist_ok=True)

        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)