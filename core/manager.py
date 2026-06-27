import time
from core.storage import Storage
from ui.note_window import NoteWindow


class NoteManager:

    def __init__(self):
        self.windows = []
        self.data = Storage.load()

    def load_all(self):
        for d in self.data:
            self.create(d)

    def create(self, data=None):
        note_id = int(time.time() * 1000)

        d = data or {
            "id": note_id,
            "text": "",
            "x": 200,
            "y": 200,
            "width": 300,
            "height": 250
        }

        win = NoteWindow(d, self)
        self.windows.append(win)
        win.show()

        self.save()

    def delete(self, note_id):
        self.windows = [w for w in self.windows if w.note_id != note_id]
        self.save()

    def save(self):
        data = []

        for w in self.windows:
            data.append({
                "id": w.note_id,
                "text": w.text.toPlainText(),
                "x": w.x(),
                "y": w.y(),
                "width": w.width(),
                "height": w.height()
            })

        Storage.save(data)