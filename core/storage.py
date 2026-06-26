import os
import sys

def base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


FILE = os.path.join(base_path(), "data", "notes.json")


class Storage:

    @staticmethod
    def load():
        if not os.path.exists(FILE):
            return []
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def save(data):
        os.makedirs("data", exist_ok=True)
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
