from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt


class NoteWindow(QWidget):

    def __init__(self, note_id, data, manager):
        super().__init__()

        self.note_id = note_id
        self.manager = manager

        self.setWindowTitle("Sticky Note")
        self.resize(data.get("width", 300), data.get("height", 250))
        self.move(data.get("x", 200), data.get("y", 200))

        self.text = QTextEdit()
        self.text.setText(data.get("text", ""))

        self.text.textChanged.connect(self.save)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

    def save(self):
        self.manager.save()

    def moveEvent(self, event):
        self.manager.save()
        super().moveEvent(event)

    def resizeEvent(self, event):
        self.manager.save()
        super().resizeEvent(event)

    def closeEvent(self, event):
        self.manager.delete_note(self.note_id)
        event.accept()
