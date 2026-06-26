from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6.QtGui import QIcon, QAction


class Tray:

    def __init__(self, manager):
        self.manager = manager

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("resources/icon.ico"))

        menu = QMenu()

        new_note = QAction("새 메모")
        new_note.triggered.connect(self.manager.create_note)

        show_all = QAction("모든 메모 표시")
        show_all.triggered.connect(self.show_all)

        hide_all = QAction("모든 메모 숨기기")
        hide_all.triggered.connect(self.hide_all)

        quit_app = QAction("종료")
        quit_app.triggered.connect(QApplication.quit)

        menu.addAction(new_note)
        menu.addAction(show_all)
        menu.addAction(hide_all)
        menu.addSeparator()
        menu.addAction(quit_app)

        self.tray.setContextMenu(menu)
        self.tray.show()

    def show_all(self):
        for w in self.manager.windows:
            w.show()

    def hide_all(self):
        for w in self.manager.windows:
            w.hide()
