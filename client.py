# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Sun Dec  4 18:34:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-04
-- Learning how Sockets work! --
"""

from PySide import QtCore, QtGui

class Ui_Client(object):
    """
    server.ui file converted to server.py file via pyside
    """
    def setupUi(self, Client):
        """
        gui-configuration
        :param Client:
        :return:
        """
        Client.setObjectName("Client")
        Client.resize(459, 347)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Client)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Client)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(Client)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtGui.QPushButton(Client)
        self.pushButton.setMinimumSize(QtCore.QSize(439, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtGui.QLabel(Client)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textBrowser = QtGui.QTextBrowser(Client)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        """
        translating client-gui
        :param Client:
        :return:
        """
        Client.setWindowTitle(QtGui.QApplication.translate("Client", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Client", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Client", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Client", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

