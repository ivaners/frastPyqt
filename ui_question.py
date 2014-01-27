# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'question.ui'
#
# Created: Sun Jan 26 11:04:11 2014
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

class Ui_Question(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(404, 364)
        Dialog.setFixedSize(410, 365)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 361, 331))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.title = QtGui.QLineEdit(self.groupBox)
        self.title.setGeometry(QtCore.QRect(20, 50, 321, 20))
        self.title.setObjectName(_fromUtf8("title"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.content = QtGui.QTextEdit(self.groupBox)
        self.content.setGeometry(QtCore.QRect(20, 100, 321, 131))
        self.content.setObjectName(_fromUtf8("content"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.vcodeimg = QtGui.QLabel(self.groupBox)
        self.vcodeimg.setGeometry(QtCore.QRect(130, 250, 100, 40))
        self.vcodeimg.setText(_fromUtf8(""))
        self.vcodeimg.setObjectName(_fromUtf8("vcodeimg"))
        self.vcode = QtGui.QLineEdit(self.groupBox)
        self.vcode.setGeometry(QtCore.QRect(20, 270, 91, 20))
        self.vcode.setObjectName(_fromUtf8("vcode"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "知道-提问", None))
        self.groupBox.setTitle(_translate("Dialog", "提问", None))
        self.label.setText(_translate("Dialog", "标题（50字以内）", None))
        self.label_2.setText(_translate("Dialog", "详细问题描述", None))
        self.pushButton.setText(_translate("Dialog", "提交问题", None))
        self.label_4.setText(_translate("Dialog", "验证码", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Question()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

