''' This is class JavaLoader, interface for JavaLoader 

RIM Wireless Handheld Java Loader
Copyright 2001-2009 Research In Motion Limited

Usage: JavaLoader [-p<pin>] [-d0|-d1] [-w<password>] [-q] <command>

-p<pin>      Specifies the handheld PIN (hex pin prefix '0x')
-d0          Disables VM debug mode
-d1          Enables VM debug mode
-w<password> Connects using the specified password
-q           Quiet mode

<command> is one of

  dir [-d] [-s] [-1]
    Lists modules on the handheld
      -d     Display dependency information
      -s     Display siblings
      -1     Single column output

  deviceinfo
    Provides information on the handheld

  load <.cod file> ...
    Loads modules onto the handheld

  load <.jad file>
    Load modules described by JAD onto the handheld

  load @<manifest> ...
    Loads all modules named in <manifest> onto the handheld

  save { <module> ... | -g <group> }
    Retrieves modules from the handheld
      -g     Retrieves all modules in a specified group

  info [-d] [-s] [-v] <.cod file> ...
    Provides information on the specified modules
      -d     Display dependency information
      -s     Display sibling information
      -v     Display verbose module information

  wipe [-a|-f]
    Wipes the handheld
      -a     Wipe applications only
      -f     Wipe filesystem only

  erase [-f] { <module> ... | -g <group> }
    Erases modules on the handheld
      -f     Force erase of in-use modules
      -g     Erases all modules in a specified group

  debugmode
    Enables VM debug mode

  eventlog
    Retrives the handheld event log

  cleareventlog
    Clears the handheld event log

  settime
    Sets the time on the handheld to the current time

  radio on|off
    Turns the handheld's radio on or off

  enum
    Enumerates all USB handhelds

  siblinginfo <.cod file> ...
    Provides sibling information on the specified modules

  screenshot [active|primary|auxiliary] <.bmp file>
    Retreives the current contents of the specified screen
    and saves it as a BMP file. If the screen is not
    specified, the default is "active".

  logstacktraces
    Dumps the stack traces for all threads to the event log

  resettofactory
    Reset IT policy to factory settings
    (Wipes all user data)

  recoverflash <size in bytes>
    Attempts to recover the specified amount of flash
'''

import os

class JavaLoader(object):
    
    CURRPATH = os.getcwd()
    JAVALOADER = "JavaLoader.exe"
    JAVALOADER_PATH = "%s\\%s" % (CURRPATH,  JAVALOADER)
    COMMANDS = {'Device Info': 'deviceinfo',
            'Event Log': 'eventlog',
            'Wipe Device': 'wipe',
            'Reset to Factory': 'resettofactory', 
            'Screenshot': 'screenshot', 
            'Load': 'load', 
            'Save': 'save', 
            'Dir': 'dir',
            'Info': 'info',
            'Erase': 'erase',
            'Clear Event Log': 'cleareventlog',
            'Set Time': 'settime'}
            
    def __init__(self):
        self.password = None
        self.command = None
            
    def createCommand(self, command, *args):
        other_options = ' '.join([arg for arg in args])
        try:
            if self.password is None:
                return ' '.join([self.JAVALOADER_PATH, self.COMMANDS[command], other_options]).strip()
            else:
                pass_option = '-w%s'%(self.password)
                return ' '.join([self.JAVALOADER_PATH, pass_option, self.COMMANDS[command], other_options]).strip()
        except KeyError:
            pass
    
    def run(self,  command,  *args):
        from subprocess import Popen, PIPE
        self.command = self.createCommand(command,  *args)
        try:
            p = Popen(self.command,  stdout=PIPE,  stderr=PIPE)
            return p
        except:
            return None
