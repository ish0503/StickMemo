from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt

from core.storage import Storage


class NoteWindow(QWidget):

    def __init__(self, note_id=None, data=None):
        super().__init__()

        self.note_id = note_id
        self.data = data or {}

        self.setWindowTitle("Sticky Note")
        self.resize(
            self.data.get("width", 300),
            self.data.get("height", 250)
        )

        # 위치 복원
        if "x" in self.data and "y" in self.data:
            self.move(self.data["x"], self.data["y"])

        self.text = QTextEdit()
        self.text.setText(self.data.get("text", ""))

        self.text.textChanged.connect(self.save)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

    # 창 이동 감지
    def moveEvent(self, event):
        self.save()
        super().moveEvent(event)

    # 창 크기 변경 감지
    def resizeEvent(self, event):
        self.save()
        super().resizeEvent(event)

    # 자동 저장
    def save(self):
        notes = Storage.load_notes()

        found = False

        for n in notes:
            if n["id"] == self.note_id:
                n["text"] = self.text.toPlainText()
                n["x"] = self.x()
                n["y"] = self.y()
                n["width"] = self.width()
                n["height"] = self.height()
                found = True
                break

        if not found:
            notes.append({
                "id": self.note_id,
                "text": self.text.toPlainText(),
                "x": self.x(),
                "y": self.y(),
                "width": self.width(),
                "height": self.height()
            })

        Storage.save_notes(notes)
