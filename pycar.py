#!/usr/bin/env python

import os
import sys
from PyQt4 import QtCore, QtGui
from login import Ui_Form
from main import Ui_Main
from bootup import Ui_Bootup
from pythonwifi.iwlibs import Wireless

class BootupForm(QtGui.QMainWindow):

  launchTimer = 15

  def updateStates(self):
    try:
      wifi = Wireless('wlan0')
      ap_addr = wifi.getAPaddr()

      # Update Wifi Status
      if (ap_addr == "00:00:00:00:00:00"):
        self.ui.lblWifiStatus.setText('Not associated')
      else:
        self.ui.lblWifiStatus.setText(str(wifi.getEssid())+" connected")

      # Update 3G status
      ## Grep for route here

      # Update internet connectivity status
      response = os.system("ping -c 1 google.co.uk > /dev/null")
      if response == 0:
        self.ui.lblNetStatus.setText('Connected')
        netConnected = 1
      else:
        self.ui.lblNetStatus.setText('Not Connected')
        netConnected = 0

      # Update chef status
      response = os.system("ps auwwwx | grep -q chef-client")
      if response == 1:
        self.ui.lblChefRunStatus.setText('Running...')
      else:
        self.ui.lblChefRunStatus.setText('Not Running')
      try:
        f = open('/tmp/chef-lastrun')
        self.ui.lblChefStatus.setText(f.read())
        f.close()
      except:
        self.ui.lblChefStatus.setText('Unable to read')
      
      if netConnected:
        self.launchTimer = self.launchTimer - 1
        self.ui.btnLaunch.setEnabled(True)
      else:
        self.launchTimer = 15
        self.ui.btnLaunch.setEnabled(False)

      if self.launchTimer == 0:
        self.LoginForm = LoginForm()
        self.LoginForm.show()
        self.hide()

      self.ui.btnLaunch.setText("Launch ("+str(self.launchTimer)+")")
  
    finally:
      QtCore.QTimer.singleShot(1000, self.updateStates)

  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Bootup()
    self.ui.setupUi(self)
    self.updateStates()
    if os.path.exists('.fullscreen'):
      self.showFullScreen()
    
class MainForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Main()
    self.ui.setupUi(self)
    if os.path.exists('.fullscreen'):
      self.showFullScreen()

class LoginForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    if os.path.exists('.fullscreen'):
      self.showFullScreen()
    QtCore.QObject.connect(self.ui.txtCode, QtCore.SIGNAL("returnPressed()"), self.check_code)

  def read_codes(self):
    try:
      with open('codes') as f:
        lines = f.read().splitlines()
    except:
      lines = ["error"]
    return lines

  def check_code(self):
    code = self.ui.txtCode.text()
    validcodes = self.read_codes()
    if "error" in validcodes:
      self.ui.lblStatus.setText("An error occured reading codes")
    elif code in validcodes:
      self.ui.lblStatus.setText("Code accepted")
      self.mainform = MainForm()
      self.mainform.show()
      self.hide()
    else:
      self.ui.lblStatus.setText("Code invalid")
    self.ui.txtCode.setText("")

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = BootupForm()
  myapp.show()
  sys.exit(app.exec_())
