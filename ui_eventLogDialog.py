# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\mico\Documents\Projects\sandbox\jl\eventLogDialog.ui'
#
# Created: Sun Aug 01 05:15:18 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_eventLogDialog(object):
    def setupUi(self, eventLogDialog):
        eventLogDialog.setObjectName("eventLogDialog")
        eventLogDialog.resize(482, 405)
        self.eventLogScrollArea = QtGui.QScrollArea(eventLogDialog)
        self.eventLogScrollArea.setGeometry(QtCore.QRect(20, 20, 431, 321))
        self.eventLogScrollArea.setWidgetResizable(True)
        self.eventLogScrollArea.setObjectName("eventLogScrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.eventLogScrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 429, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.eventLogTextEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.eventLogTextEdit.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.eventLogTextEdit.setReadOnly(True)
        self.eventLogTextEdit.setObjectName("eventLogTextEdit")
        self.eventLogScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.okPushButton = QtGui.QPushButton(eventLogDialog)
        self.okPushButton.setGeometry(QtCore.QRect(120, 360, 93, 28))
        self.okPushButton.setObjectName("okPushButton")
        self.saveEventLogPushButton = QtGui.QPushButton(eventLogDialog)
        self.saveEventLogPushButton.setGeometry(QtCore.QRect(250, 360, 111, 28))
        self.saveEventLogPushButton.setObjectName("saveEventLogPushButton")

        self.retranslateUi(eventLogDialog)
        QtCore.QMetaObject.connectSlotsByName(eventLogDialog)

    def retranslateUi(self, eventLogDialog):
        eventLogDialog.setWindowTitle(QtGui.QApplication.translate("eventLogDialog", "Event Log", None, QtGui.QApplication.UnicodeUTF8))
        self.okPushButton.setText(QtGui.QApplication.translate("eventLogDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.saveEventLogPushButton.setText(QtGui.QApplication.translate("eventLogDialog", "Save Event Log", None, QtGui.QApplication.UnicodeUTF8))

