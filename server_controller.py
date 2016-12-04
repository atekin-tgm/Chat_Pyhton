"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-04
-- Learning how Sockets work! --
"""

import client, server, socket, sys, threading
from PySide import QtCore, QtGui

# Much Wellner Help

class ServerController(threading.Thread, QtGui.QWidget):

    def __init__(self, parent=None):
        '''

        :param parent:
        '''
        super().__init__(parent)
        threading.Thread.__init__(self)

        self.view = server.Ui_Server()
        self.view.setupUi(self)

        self.host = "localhost"
        self.port = 50000

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

        self.socket.listen(5)


    def run(self):
        '''

        :return:
        '''
        try:
            while True:
                print("Auf client warten...")
                (clientsocket, address) = self.socket.accept()
                print("Client verbunden! Warte auf Nachricht...")

                while True:
                    data = clientsocket.recv(1024).decode()

                    if not data:
                        clientsocket.close()
                        break
                    if data == "exit":
                        clientsocket.send("Adios!".encode())
                        clientsocket.close()
                        break
                    else:
                        msg = input("Antwort an Client: ")
                        clientsocket.send(msg.encode())

        except socket.error as SocketError:
            print("Socket closed!")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    t = ServerController()
    t.show()

    t.start()

    t.join()

    sys.exit(app.exec_())
