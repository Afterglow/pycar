# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Fri Dec 14 01:34:40 2012
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 480)
        self.lblUser = QtGui.QLabel(Form)
        self.lblUser.setGeometry(QtCore.QRect(10, 110, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lblUser.setFont(font)
        self.lblUser.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUser.setObjectName(_fromUtf8("lblUser"))
        self.lblWelcome = QtGui.QLabel(Form)
        self.lblWelcome.setGeometry(QtCore.QRect(10, 30, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setTextFormat(QtCore.Qt.PlainText)
        self.lblWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWelcome.setObjectName(_fromUtf8("lblWelcome"))
        self.txtCode = QtGui.QLineEdit(Form)
        self.txtCode.setGeometry(QtCore.QRect(160, 160, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtCode.setFont(font)
        self.txtCode.setText(_fromUtf8(""))
        self.txtCode.setObjectName(_fromUtf8("txtCode"))
        self.lblStatus = QtGui.QLabel(Form)
        self.lblStatus.setGeometry(QtCore.QRect(11, 240, 621, 20))
        self.lblStatus.setText(_fromUtf8(""))
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lblUser.setText(_translate("Form", "Please login to authenticate", None))
        self.lblWelcome.setText(_translate("Form", "Welcome...", None))

