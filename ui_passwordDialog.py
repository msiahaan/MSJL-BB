# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mico\Documents\Projects\sandbox\jl\passwordDialog.ui'
#
# Created: Sun Aug 01 05:15:18 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_passwordDialog(object):
    def setupUi(self, passwordDialog):
        passwordDialog.setObjectName("passwordDialog")
        passwordDialog.resize(367, 155)
        self.okNoButtonBox = QtGui.QDialogButtonBox(passwordDialog)
        self.okNoButtonBox.setGeometry(QtCore.QRect(30, 110, 291, 32))
        self.okNoButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.okNoButtonBox.setStandardButtons(QtGui.QDialogButtonBox.No|QtGui.QDialogButtonBox.Ok)
        self.okNoButtonBox.setObjectName("okNoButtonBox")
        self.passwordLineEdit = QtGui.QLineEdit(passwordDialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(30, 70, 291, 22))
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLabel = QtGui.QLabel(passwordDialog)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 20, 321, 41))
        self.passwordLabel.setWordWrap(True)
        self.passwordLabel.setObjectName("passwordLabel")

        self.retranslateUi(passwordDialog)
        QtCore.QObject.connect(self.okNoButtonBox, QtCore.SIGNAL("accepted()"), passwordDialog.accept)
        QtCore.QObject.connect(self.okNoButtonBox, QtCore.SIGNAL("rejected()"), passwordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(passwordDialog)

    def retranslateUi(self, passwordDialog):
        passwordDialog.setWindowTitle(QtGui.QApplication.translate("passwordDialog", "Enter Password", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("passwordDialog", "Please Enter Device Password. If device has no password just click \'No\'", None, QtGui.QApplication.UnicodeUTF8))

