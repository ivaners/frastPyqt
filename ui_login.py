# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Jan 25 15:06:28 2014
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

class Ui_Login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(335, 184)
        Dialog.setFixedSize(335, 184)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 301, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 60, 75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(20, 20, 175, 121))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.userName = QtGui.QLineEdit(self.layoutWidget)
        self.userName.setObjectName(_fromUtf8("userName"))
        self.gridLayout_2.addWidget(self.userName, 0, 1, 1, 1)
        self.password = QtGui.QLineEdit(self.layoutWidget)
        self.password.setMinimumSize(QtCore.QSize(113, 0))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout_2.addWidget(self.password, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(54, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.vcode = QtGui.QLineEdit(self.layoutWidget)
        self.vcode.setObjectName(_fromUtf8("vcode"))
        self.gridLayout_2.addWidget(self.vcode, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.vcodeImg = QtGui.QLabel(self.splitter)
        self.vcodeImg.setEnabled(True)
        self.vcodeImg.setMinimumSize(QtCore.QSize(0, 40))
        self.vcodeImg.setMaximumSize(QtCore.QSize(100, 40))
        self.vcodeImg.setText(_fromUtf8(""))
        self.vcodeImg.setObjectName(_fromUtf8("vcodeImg"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "百度知道登录", None))
        self.groupBox.setTitle(_translate("Dialog", "登录", None))
        self.pushButton.setText(_translate("Dialog", "登录", None))
        self.label_2.setText(_translate("Dialog", "密 码", None))
        self.label.setText(_translate("Dialog", "帐 号", None))
        self.label_3.setText(_translate("Dialog", "验证码", None))


if __name__ == "__main__":
    import sys
    import urllib,urllib2
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    pixmap = QtGui.QPixmap()
    url = 'https://passport.baidu.com/cgi-bin/genimage?captchaservice633162343358332f4b6156474b5a596e334159484c575135696f34744c54376175366b6c54536c444341533477556c547a564851316859516a6e506b50302f716e4d4f327a52756662676e6f4971524845664d7549563433554672572b394b6255704b6d525557654350626e684f66536635412b776431716e4d6a4f37676d37366f335a36544d51683678474b67756c46324137694e534839525865564e412f76797141574e683173736d336757596d5a44767034586141304465564e5a792f74637130315337745249554f58724e46325a597a65796d514b2f58364b414844775a6147307848685268735650314565674f4c47584a546e7369464866556e747438746f41736b666f366d6d2b65647975364f302b52443374343050575a57546942456b457458357a35746552386f43542f4a483536664f765a382b75625251'
    pixmap.loadFromData(urllib.urlopen(url).read())
    ui.vcodeImg.setPixmap(pixmap)
    Dialog.show()
    sys.exit(app.exec_())

