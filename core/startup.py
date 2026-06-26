import winreg
import sys


def add_to_startup():
    path = sys.executable

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )

    winreg.SetValueEx(key, "StickyNotes", 0, winreg.REG_SZ, path)
    winreg.CloseKey(key)
