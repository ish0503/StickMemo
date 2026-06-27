import os
import sys

LOCK_FILE = "lock/app.lock"


class InstanceLock:

    def __init__(self):
        self.is_primary = False
        self.lock_path = self._get_path()

        os.makedirs(os.path.dirname(self.lock_path), exist_ok=True)

        if os.path.exists(self.lock_path):
            self.is_primary = False
        else:
            self.is_primary = True
            with open(self.lock_path, "w") as f:
                f.write(str(os.getpid()))

    def _get_path(self):
        if getattr(sys, 'frozen', False):
            base = os.path.dirname(sys.executable)
        else:
            base = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base, LOCK_FILE)

    def remove(self):
        try:
            if os.path.exists(self.lock_path):
                os.remove(self.lock_path)
        except:
            pass