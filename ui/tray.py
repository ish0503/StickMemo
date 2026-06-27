from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication
from PySide6.QtGui import QAction, QIcon


class Tray:

    def __init__(self, manager):

        self.manager = manager

        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("resources/icon.ico"))

        menu = QMenu()

        new_note = QAction("새 메모")
        new_note.triggered.connect(self.manager.create)

        quit_app = QAction("종료")
        quit_app.triggered.connect(QApplication.quit)

        menu.addAction(new_note)
        menu.addSeparator()
        menu.addAction(quit_app)

        self.tray.setContextMenu(menu)
        self.tray.show()