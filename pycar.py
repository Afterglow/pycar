#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from login import Ui_Form

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
#    self.showFullScreen()
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
    else:
      self.ui.lblStatus.setText("Code invalid")
    self.ui.txtCode.setText("")

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
