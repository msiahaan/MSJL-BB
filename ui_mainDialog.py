# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mico\Documents\Projects\sandbox\jl\mainDialog.ui'
#
# Created: Sun Aug 01 05:01:32 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName("mainDialog")
        mainDialog.resize(285, 429)
        self.deviceInfoPushbutton = QtGui.QPushButton(mainDialog)
        self.deviceInfoPushbutton.setGeometry(QtCore.QRect(40, 30, 201, 31))
        self.deviceInfoPushbutton.setObjectName("deviceInfoPushbutton")
        self.eventLogPushButton = QtGui.QPushButton(mainDialog)
        self.eventLogPushButton.setGeometry(QtCore.QRect(40, 80, 201, 31))
        self.eventLogPushButton.setObjectName("eventLogPushButton")
        self.takeScreenshotPushButton = QtGui.QPushButton(mainDialog)
        self.takeScreenshotPushButton.setGeometry(QtCore.QRect(40, 130, 201, 31))
        self.takeScreenshotPushButton.setObjectName("takeScreenshotPushButton")
        self.wipeDevicePushButton = QtGui.QPushButton(mainDialog)
        self.wipeDevicePushButton.setGeometry(QtCore.QRect(40, 180, 201, 31))
        self.wipeDevicePushButton.setObjectName("wipeDevicePushButton")
        self.quitPushButton = QtGui.QPushButton(mainDialog)
        self.quitPushButton.setGeometry(QtCore.QRect(90, 360, 93, 28))
        self.quitPushButton.setObjectName("quitPushButton")
        self.launchLoaderPushButton = QtGui.QPushButton(mainDialog)
        self.launchLoaderPushButton.setGeometry(QtCore.QRect(40, 310, 201, 28))
        self.launchLoaderPushButton.setObjectName("launchLoaderPushButton")
        self.resetFactoryPushButton = QtGui.QPushButton(mainDialog)
        self.resetFactoryPushButton.setGeometry(QtCore.QRect(40, 230, 201, 28))
        self.resetFactoryPushButton.setObjectName("resetFactoryPushButton")

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QtGui.QApplication.translate("mainDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceInfoPushbutton.setText(QtGui.QApplication.translate("mainDialog", "Device Info", None, QtGui.QApplication.UnicodeUTF8))
        self.eventLogPushButton.setText(QtGui.QApplication.translate("mainDialog", "Event Log", None, QtGui.QApplication.UnicodeUTF8))
        self.takeScreenshotPushButton.setText(QtGui.QApplication.translate("mainDialog", "Take Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.wipeDevicePushButton.setText(QtGui.QApplication.translate("mainDialog", "Wipe Device", None, QtGui.QApplication.UnicodeUTF8))
        self.quitPushButton.setText(QtGui.QApplication.translate("mainDialog", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.launchLoaderPushButton.setText(QtGui.QApplication.translate("mainDialog", "Install OS (Launch Loader)", None, QtGui.QApplication.UnicodeUTF8))
        self.resetFactoryPushButton.setText(QtGui.QApplication.translate("mainDialog", "Reset to Factory Settings", None, QtGui.QApplication.UnicodeUTF8))

