import sys
from PySide6.QtWidgets import QApplication

from ui.note_window import NoteWindow
from core.storage import Storage


def main():
    app = QApplication(sys.argv)

    notes = Storage.load_notes()

    windows = []

    # 저장된 메모 복원
    for note in notes:
        win = NoteWindow(note_id=note["id"], data=note)
        win.show()
        windows.append(win)

    # 저장이 하나도 없으면 기본 메모 1개 생성
    if not windows:
        win = NoteWindow(note_id=1)
        win.show()
        windows.append(win)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
