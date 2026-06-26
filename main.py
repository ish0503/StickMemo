import sys
from PySide6.QtWidgets import QApplication

from core.manager import NoteManager
from ui.tray import Tray


def main():
    app = QApplication(sys.argv)

    manager = NoteManager()

    tray = Tray(manager)

    # 기존 메모 불러오기
    manager.load_all()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
