import sys
from PySide6.QtWidgets import QApplication

from core.manager import NoteManager
from core.single_instance import SingleInstance
from ui.tray import Tray


def main():
    app = QApplication(sys.argv)

    instance = SingleInstance()

    # 이미 실행 중이면 종료
    if not instance.is_primary:
        instance.send_new_note_signal()
        return

    manager = NoteManager()
    manager.load_all()

    tray = Tray(manager, instance)

    # 기본 메모 없으면 생성
    if not manager.windows:
        manager.create()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
