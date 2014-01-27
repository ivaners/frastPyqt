# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baidu.ui'
#
# Created: Wed Jan 22 11:51:59 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(380, 155)
        Dialog.setFixedSize(380, 155)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 100, 40))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 50, 100, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "百度知道", None))
        self.pushButton.setText(_translate("Dialog", "提 问", None))
        self.pushButton_2.setText(_translate("Dialog", "回 答", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

