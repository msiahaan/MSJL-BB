# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mico\Documents\Projects\sandbox\jl\deviceInfoDialog.ui'
#
# Created: Sun Aug 01 05:15:18 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_deviceInfoDialog(object):
    def setupUi(self, deviceInfoDialog):
        deviceInfoDialog.setObjectName("deviceInfoDialog")
        deviceInfoDialog.resize(482, 393)
        self.deviceInfoScrollArea = QtGui.QScrollArea(deviceInfoDialog)
        self.deviceInfoScrollArea.setGeometry(QtCore.QRect(20, 20, 431, 301))
        self.deviceInfoScrollArea.setWidgetResizable(True)
        self.deviceInfoScrollArea.setObjectName("deviceInfoScrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.deviceInfoScrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.deviceInfoTextEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.deviceInfoTextEdit.setGeometry(QtCore.QRect(10, 10, 411, 281))
        self.deviceInfoTextEdit.setReadOnly(True)
        self.deviceInfoTextEdit.setObjectName("deviceInfoTextEdit")
        self.deviceInfoScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.okPushButton = QtGui.QPushButton(deviceInfoDialog)
        self.okPushButton.setGeometry(QtCore.QRect(120, 350, 93, 28))
        self.okPushButton.setObjectName("okPushButton")
        self.saveInfoPushButton = QtGui.QPushButton(deviceInfoDialog)
        self.saveInfoPushButton.setGeometry(QtCore.QRect(240, 350, 121, 28))
        self.saveInfoPushButton.setObjectName("saveInfoPushButton")

        self.retranslateUi(deviceInfoDialog)
        QtCore.QMetaObject.connectSlotsByName(deviceInfoDialog)

    def retranslateUi(self, deviceInfoDialog):
        deviceInfoDialog.setWindowTitle(QtGui.QApplication.translate("deviceInfoDialog", "Device Info", None, QtGui.QApplication.UnicodeUTF8))
        self.okPushButton.setText(QtGui.QApplication.translate("deviceInfoDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.saveInfoPushButton.setText(QtGui.QApplication.translate("deviceInfoDialog", "Save Device Info", None, QtGui.QApplication.UnicodeUTF8))

