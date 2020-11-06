#!/usr/bin/env python

import sys
import os
from subprocess import Popen, PIPE

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_mainDialog
import ui_deviceInfoDialog
import ui_eventLogDialog
import ui_passwordDialog

from JavaLoader import JavaLoader

__version__ = '0.3'

HOMEPATH = os.environ['HOMEPATH']

# instance of JavaLoader

jl = JavaLoader() 

class MainDialog(QDialog, ui_mainDialog.Ui_mainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.callPasswordDialog()
        self.setupUi(self)
        self.setWindowTitle("MSJavaLoader-BB")
        
        self.connect(self.quitPushButton, SIGNAL("clicked()"), self.exit)
        self.connect(self.deviceInfoPushbutton, SIGNAL("clicked()"), self.showDeviceInfo)
        self.connect(self.eventLogPushButton, SIGNAL("clicked()"), self.showEventLog)
        self.connect(self.takeScreenshotPushButton, SIGNAL("clicked()"), self.takeScreenshot)
        self.connect(self.wipeDevicePushButton, SIGNAL("clicked()"), self.wipeDevice)
        self.connect(self.resetFactoryPushButton,  SIGNAL("clicked()"),  self.resetToFactory)
        self.connect(self.launchLoaderPushButton,  SIGNAL("clicked()"),  self.installOS)
            
    
    def exit(self):
        sys.exit()
    
    def callPasswordDialog(self):
        dialog = PasswordDialog(self)
        dialog.setWindowTitle("Enter Password")
        if dialog.exec_():
            jl.password = dialog.passwordLineEdit.text()
        else:
            jl.password = None
        
    
    def showDeviceInfo(self):
        dialog = DeviceInfoDialog(self)
        try:
            p = jl.run('Device Info')
            dialog.deviceInfoText = p.communicate()[0]
            dialog.deviceInfoTextEdit.setText(str(dialog.deviceInfoText))
        except:
            pass
            
        dialog.setWindowTitle("Device Info")
        dialog.exec_()
    
    
    def showEventLog(self):
        dialog = EventLogDialog(self)
        try:
            p = jl.run('Event Log')
            dialog.eventLogText = p.communicate()[0]
            dialog.eventLogTextEdit.setText(str(dialog.eventLogText))
        except:
            pass
        
        dialog.setWindowTitle("Event Log")
        dialog.exec_()
    
    
    def takeScreenshot(self):
        
        fileName = QFileDialog.getSaveFileName(self, "Save Screenshot",  HOMEPATH,  "All files (*.*)")
        try:
            p = jl.run('Screenshot',  str(fileName))
            p.communicate()
            QMessageBox.information(self, "Screenshot Success!", '''Take screenshot successfully! It has been saved in %s''' % fileName)
        except:
            pass
        
    
    def wipeDevice(self):
        respond = QMessageBox.warning(self, "Wipe Device", "Are you sure to wipe this device?",
                            buttons = QMessageBox.Ok|QMessageBox.Cancel)
        if respond == QMessageBox.Ok:
            try:
                p = jl.run('Wipe Device')
                p.communicate()
                QMessageBox.information(self, "Wipe Device Success!", '''Wipe Device successfully!''')
            except:
                pass
        elif respond == QMessageBox.Cancel:
            pass
    
    def resetToFactory(self):  
        respond = QMessageBox.warning(self, "Reset to Factory Settings", "Are you sure to reset to factory settings?",
                            buttons = QMessageBox.Ok|QMessageBox.Cancel)
        if respond == QMessageBox.Ok:
            try:
                p = jl.run('Reset To Factory')
                p.communicate()
                QMessageBox.information(self, "Reset to Factory Settings Success!", '''Reset to factory settings successfully!''')
            except:
                pass
        elif respond == QMessageBox.Cancel:
            pass
            

    def installOS(self):
        import _winreg as winreg
        # open RIM Apploader Key
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Research In Motion\AppLoader')
        value, type_id = winreg.QueryValueEx(key, 'Path') # get Apploader path value
        loader_path = value + u'Loader.exe'
        try:
            import win32api
            win32api.WinExec(loader_path)
        except:
            QMessageBox.information(self, "Loader not found!", '''Loader.exe Not Found!
                \nPlease reinstall Blackberry Desktop Software''')

    
class DeviceInfoDialog(QDialog, ui_deviceInfoDialog.Ui_deviceInfoDialog):
    def __init__(self, parent=None):
        super(DeviceInfoDialog, self).__init__(parent)
        self.deviceInfoText = 'Device Info: None'
        self.setupUi(self)
        self.connect(self.okPushButton, SIGNAL("clicked()"), self.close)
        self.connect(self.saveInfoPushButton,  SIGNAL("clicked()"),  self.saveInfo)
        
    def saveInfo(self):
        fileName = QFileDialog.getSaveFileName(self, "Save Device Info",  HOMEPATH,  "Text Files (*.txt)")
        try:
            file = open(fileName,  'w')
            file.writelines(self.deviceInfoText)
        except IOError:
            pass



class EventLogDialog(QDialog, ui_eventLogDialog.Ui_eventLogDialog):
    def __init__(self, parent=None):
        super(EventLogDialog, self).__init__(parent)
        self.eventLogText = 'Event Log: None'
        self.setupUi(self)
        self.connect(self.okPushButton, SIGNAL("clicked()"), self.close)
        self.connect(self.saveEventLogPushButton,  SIGNAL("clicked()"),  self.saveEventLog)
        
    def saveEventLog(self):
        homepath = os.environ['HOMEPATH']
        fileName = QFileDialog.getSaveFileName(self, "Save Event Log",  HOMEPATH,  "Text Files (*.txt)")
        try:
            file = open(fileName,  'w')
            file.writelines(self.eventLogText)
        except IOError:
            pass



class PasswordDialog(QDialog, ui_passwordDialog.Ui_passwordDialog):
    def __init__(self, parent=None):
        super(PasswordDialog, self).__init__(parent)
        self.setupUi(self)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()
