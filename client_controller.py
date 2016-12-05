"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-04
-- Learning how Sockets work! --
"""

import client, server, socket, sys, threading
from PySide import QtCore, QtGui

#Much Wellner Help

class ClientController(threading.Thread, QtGui.QWidget):
    """
    Controller for the Client
    connects with client_view
    :inheritance threading.Thread:
    :inheritance QtGui.QWidget:
    """
    def __init__(self, parent=None):
        """
        Constructor of ClientController class
        :param parent:
        """
        threading.Thread.__init__(self)
        QtGui.QWidget.__init__(self)

        self.view = client.Ui_Client()
        self.view.setupUi(self)

        self.msg = ""
        self.button()

        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        """
        connects to the server
        tells server what the hostname and the port is
        :return None:
        """
        try:
            self.clientsocket.connect(("localhost", 50000))

            while True:
                self.clientsocket.send(self.msg.encode())

                data = self.clientsocket.recv(1024).decode()

                print("Server: " + data)

        except socket.error as SocketError:
            print("Socketerror: " + SocketError.strerror)


    def button(self):
        """
        if button clicked -> message is sent
        :return:
        """
        self.view.pushButton.clicked.connect(lambda: self.setmsg("Client 1: " + self.view.textEdit.text()))
        #nie wieder hilfe von Wellner nehmen!!!

    def setmsg(self, msg):
        """
        message is given to chat
        :param msg:
        :return:
        """
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