import sys
from PySide6.QtWidgets import QApplication

from core.manager import NoteManager
from core.instance_lock import InstanceLock
from ui.tray import Tray


def main():
    app = QApplication(sys.argv)

    lock = InstanceLock()

    # 이미 실행 중이면 종료
    if not lock.is_primary:
        return

    manager = NoteManager()
    manager.load_all()

    tray = Tray(manager)

    if not manager.windows:
        manager.create()

    exit_code = app.exec()

    lock.remove()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()