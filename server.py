# -*- coding: utf-8 -*-

# Server implementation generated from reading ui file 'Server.ui'
#
# Created: Sun Dec  4 18:35:16 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(458, 339)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Server)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Server)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtGui.QTextBrowser(Server)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.label_2 = QtGui.QLabel(Server)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textBrowser_2 = QtGui.QTextBrowser(Server)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def retranslateUi(self, Server):
        Server.setWindowTitle(QtGui.QApplication.translate("Server", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Server", "Online:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Server", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

