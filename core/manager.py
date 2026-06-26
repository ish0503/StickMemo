import time
from core.storage import Storage
from ui.note_window import NoteWindow


class NoteManager:

    def __init__(self):
        self.windows = []
        self.notes = Storage.load_notes()

    def create_note(self, data=None):
        note_id = int(time.time() * 1000)

        note_data = data or {
            "id": note_id,
            "text": "",
            "x": 200,
            "y": 200,
            "width": 300,
            "height": 250
        }

        window = NoteWindow(note_id=note_id, data=note_data, manager=self)

        self.windows.append(window)
        window.show()

        self.save()

    def delete_note(self, note_id):
        self.windows = [w for w in self.windows if w.note_id != note_id]

        self.notes = [n for n in self.notes if n["id"] != note_id]

        Storage.save_notes(self.notes)

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

        Storage.save_notes(data)

    def load_all(self):
        for note in self.notes:
            self.create_note(note)
