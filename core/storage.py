import json
import os

DATA_FILE = os.path.join("data", "notes.json")


class Storage:

    @staticmethod
    def load_notes():
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []

    @staticmethod
    def save_notes(notes):
        os.makedirs("data", exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=4)
