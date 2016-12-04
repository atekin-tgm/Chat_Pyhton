"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-04
-- Learning how Sockets work! --
"""

import client, server, socket, sys, threading
from PySide import QtCore, QtGui

# Much Wellner Help

class ClientController(threading.Thread, QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        threading.Thread.__init__(self)

        self.view = client.Ui_Client()
        self.view.setupUi(self)

        self.msg = ""
        self.button()

        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        try:
            self.clientsocket.connect(("localhost", 50000))

            while True:
                self.clientsocket.send(self.button.encode())

                data = self.clientsocket.recv(1024).decode()

                print("Server: " + data)

        except socket.error as SocketError:
            print("Socketerror: " + SocketError.strerror)


    def button(self):
        self.view.pushButton.clicked.connect(lambda: self.setmsg("Client 1: " + self.view.input.text()))
        return self.msg

    def setmsg(self, msg):
        self.msg += msg + "<br>"
        self.view.textBrowser.setText(self.msg)
        return self.msg


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    client2 = ClientController()
    client2.show()

    client2.start()
    client2.join()

    sys.exit(app.exec_())