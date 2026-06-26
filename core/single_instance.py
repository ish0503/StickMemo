import socket
import sys

PORT = 50555


class SingleInstance:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.bind(("127.0.0.1", PORT))
            self.sock.listen(1)
            self.is_primary = True
        except:
            self.is_primary = False

    def send_new_note_signal(self):
        try:
            s = socket.socket()
            s.connect(("127.0.0.1", PORT))
            s.send(b"new_note")
            s.close()
        except:
            pass
