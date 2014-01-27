# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer.ui'
#
# Created: Sun Jan 26 18:08:03 2014
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

class Ui_Answer(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(557, 457)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.qid = QtGui.QLineEdit(Dialog)
        self.qid.setGeometry(QtCore.QRect(30, 60, 491, 20))
        self.qid.setObjectName(_fromUtf8("qid"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.content = QtGui.QTextEdit(Dialog)
        self.content.setGeometry(QtCore.QRect(30, 130, 491, 191))
        self.content.setObjectName(_fromUtf8("content"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vcode = QtGui.QLineEdit(Dialog)
        self.vcode.setGeometry(QtCore.QRect(30, 370, 113, 20))
        self.vcode.setObjectName(_fromUtf8("vcode"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 410, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.vcodeimg = QtGui.QLabel(Dialog)
        self.vcodeimg.setGeometry(QtCore.QRect(210, 350, 100, 40))
        self.vcodeimg.setText(_fromUtf8(""))
        self.vcodeimg.setObjectName(_fromUtf8("vcodeimg"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "知道-回答", None))
        self.label.setText(_translate("Dialog", "页面url", None))
        self.label_2.setText(_translate("Dialog", "回答", None))
        self.label_3.setText(_translate("Dialog", "验证码", None))
        self.pushButton.setText(_translate("Dialog", "提交回答", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Answer()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

