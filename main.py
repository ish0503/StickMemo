import sys
from PySide6.QtWidgets import QApplication

from ui.note_window import NoteWindow


def main():
    app = QApplication(sys.argv)

    note = NoteWindow()
    note.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
