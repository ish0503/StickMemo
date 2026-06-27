from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class NoteWindow(QWidget):

    def __init__(self, data, manager):
        super().__init__()

        self.manager = manager
        self.note_id = data["id"]

        self.setWindowTitle("Sticky Note")

        self.resize(data["width"], data["height"])
        self.move(data["x"], data["y"])

        self.text = QTextEdit()
        self.text.setText(data.get("text", ""))

        self.text.textChanged.connect(self.manager.save)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setLayout(layout)

    def moveEvent(self, e):
        self.manager.save()

    def resizeEvent(self, e):
        self.manager.save()

    def closeEvent(self, e):
        self.manager.delete(self.note_id)
        e.accept()