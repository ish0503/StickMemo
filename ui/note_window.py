from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt


class NoteWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sticky Note")

        self.resize(300, 250)

        self.setMinimumSize(200, 150)

        layout = QVBoxLayout()

        self.text = QTextEdit()
        self.text.setPlaceholderText("메모를 입력하세요...")

        layout.addWidget(self.text)

        layout.setContentsMargins(5, 5, 5, 5)

        self.setLayout(layout)
