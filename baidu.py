#coding: utf-8
#-----------------------------------------------
#signBaidu 2.1 by Ricter 2013-06-14
#E-mail:canyuexiaolang@gmail.com
#Website:http://ricter.rp2.jybox.net
#-----------------------------------------------
import re,time,os
from pyquery import PyQuery as pq
import urllib,urllib2
import cookielib
import ui_baidu
import ui_login
import ui_question
import ui_answer
from PyQt4.QtGui import *
import sys

class signBaidu(object):
    mainUrl  = 'http://wapp.baidu.com'
    loginUrl = 'http://wappass.baidu.com/passport/'
    username = ''
    password = ''
    vcodestr = ''
    vcode    = ''
    tbUrl    = ''
    result   = ''
    barlist  = []
    faillist = []
    uid = ''
    content = ''
    postDict = {
        'username'    : '',
        'password'    : '',
        'submit'      : '登录',
        'isphone'     : '0',
        'vcodestr'    : '',
        'u'           : 'http%3A%2F%2Fwap.baidu.com%3Fuid%3D',
        'tpl'         : '',
        'ssid'        : '',
        'from'        : '',
        'uid'         : '',
        'pu'          : '',
        'tn'          : '',
        'bdcm'        : '',
        'type'        : '',
        'bd_page_type': ''
    }
    questionPost = {}
    loginVcodeImageUrl = ''
    answerVodeImageUrl = ''
    questionVodeImageUrl = ''
    answerPost = {}
    requestData = ''
    #获取一个保存cookie的对象
    cj = cookielib.LWPCookieJar()
    #将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    #创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    #将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
    urllib2.install_opener(opener)


    def showusrandpwd(self):
        """Show Username and Password"""
        #print 'in showusrandpwd'
        print '-' * 40
        print 'Username:',self.username, '\nPassword:',self.password
        print '-' * 40

    def getURL(self,url,data):
        """Open webpages and get the HTML code"""
        #print 'in getURL'
        req = urllib2.Request(url, data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        resp = urllib2.urlopen(req, timeout=10)
        #print 'Get Url:', url
        self.requestData = resp.read()

    def getLoginUid(self):
        """Get Login Uid"""
        #print 'in getLoginUid'
        resp = urllib2.urlopen(self.loginUrl)
        uid = re.search(r'[_0-9]{17}', resp.read())
        if uid:
            self.uid = uid.group()
            print 'Get uid success:', self.uid
        else:
            print  'Get uid fail.'

    def checkIsUidGet(self):
        """Check self.uid is defineded or not"""
        #print 'in checkIsUidGet'
        if self.uid:
            return True
        else:
            return False

    def loginBaidu(self):
        """Login Baidu bar and get infomation"""
        #print 'in loginBaidu'
        self.cj.clear()
        self.getLoginUid()
        if self.checkIsUidGet():
            self.postDict['username'] = self.username
            self.postDict['password'] = self.password
            self.postDict['uid'] = self.uid
            self.postDict['u'] = self.postDict['u'] + self.uid
            #print self.postDict
            postData = urllib.urlencode(self.postDict)
            self.getURL(self.loginUrl, postData)
            d=pq(self.requestData)
            vcodeimgUrl=d('.row-padbtm-10').find('img').attr('src')
            self.loginVcodeImageUrl = vcodeimgUrl
            if "请您输入验证码" in self.requestData:                
                self.vcodestr = vcodeimgUrl.split('?')[1]
                self.postDict['vcodestr'] = self.vcodestr
                return False

            elif "您输入的密码有误" in self.requestData:
                print 'Password WRONG!'
                return False
            elif "您输入的验证码有误" in self.requestData:
                print 'Verifycode WRONG!'  
                return False
            elif "系统错误" in self.requestData:
                print 'Unexpect Error!'  
                return False
            else:
                for line in self.requestData.split('<'):
                    if 'itj=23' in line:
                        self.tbUrl = line.split('"')[1].replace('amp;', '')
                        print 'Get Baidu Bar Url...Success!'
                        return True

        else:
            print 'Construct Post data fail.'
            return False

    def answer(self,url,postDict):
        postData = urllib.urlencode(postDict)
        self.getURL(url, postData)
        if "提交" in self.requestData:
            d=pq(self.requestData)
            vcodeimgUrl=d('.vcode-img').attr('src')
            if vcodeimgUrl:
                self.answerVodeImageUrl = vcodeimgUrl
                self.answerPost['vcodestr'] = vcodeimgUrl.split('?')[1]
                self.answerPost['vcodestr'] = re.findall(r"codestr=(.*)",postDict['vcodestr'])[0]
                return False
        return True                    

    def question(self,title,content,vcode):
        self.questionPost['vcode'] = vcode
        self.questionPost['score'] = 0
        self.questionPost['anonymous'] = 0
        self.questionPost['title'] = title
        self.questionPost['content'] = content
        postData = urllib.urlencode(self.questionPost)
        self.getURL('http://zhidao.baidu.com/msubmit/ask?ta=1&amp;pu=null&amp;cifr=null', postData)
        if "输入验证码" in self.requestData: 
            d=pq(self.requestData)
            vcodeimgUrl=d('.vcode-img').attr('src')
            self.questionVodeImageUrl = vcodeimgUrl
 
            self.questionPost['vcodestr'] = vcodeimgUrl.split('?')[1]
            self.questionPost['vcodestr'] = re.findall(r"codestr=(.*)",self.questionPost['vcodestr'])[0]
            return False       
        else:
            return True
              
#-------------------------------------------------------------------------------------------------------

def showQPanel():
    qPanelUi.setupUi(qPanel)    
    qPanelUi.pushButton.clicked.connect(sinQuestion)
    qPanel.show()

def showAPanel():
    aPanelui.setupUi(aPanel)
    aPanelui.pushButton.clicked.connect(sinAnswer)
    aPanel.show()

def sinQuestion():
    title=str(qPanelUi.title.text().toUtf8())
    content=str(qPanelUi.content.toPlainText().toUtf8())
    vcode=str(qPanelUi.vcode.text().toUtf8())
    if not login.question(title,content,vcode):
        pixmap = QPixmap()
        pixmap.loadFromData(urllib.urlopen(login.questionVodeImageUrl).read())
        qPanelUi.vcodeimg.setPixmap(pixmap)
    else:
        print login.requestData
        msgBox = QMessageBox()
        msgBox.setText(u'提交成功！')
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        qPanel.close()   
    
def sinAnswer(): 
    url='http://zhidao.baidu.com/msubmit/answer?ta=1&cifr=null'

    login.answerPost['qid'] = str(aPanelui.qid.text().toUtf8())
    login.answerPost['content'] = str(aPanelui.content.toPlainText().toUtf8())
    login.answerPost['vcode'] = str(aPanelui.vcode.text().toUtf8())
    if not login.answer(url, login.answerPost):
        tpixmap = QPixmap()
        tpixmap.loadFromData(urllib.urlopen(login.answerVodeImageUrl).read())
        aPanelui.vcodeimg.setPixmap(tpixmap)
    else:
        print login.requestData
        msgBox = QMessageBox()
        msgBox.setText(u'提交成功！')
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        aPanel.close()  

def zLogin():
    login.username = str(ui.userName.text().toUtf8()).strip()
    login.password = str(ui.password.text().toUtf8()).strip()
    login.postDict['vcode'] = str(ui.vcode.text().toUtf8())
    login.postDict['verifycode'] = login.postDict['vcode']
    main()

def main():   
    if not login.loginBaidu():
        pixmap = QPixmap()
        pixmap.loadFromData(urllib.urlopen(login.loginVcodeImageUrl).read())
        ui.vcodeImg.setPixmap(pixmap)
        return False
    if login.tbUrl:
        print '-'*67
        print 'Successful login!'
        print 'Get Baidu Bar List...'
    else:
        print signBaidu.postDict
        print "登录失败"
        return False

    Dialog.close()
    mPanelUi = ui_baidu.Ui_Dialog()
    mPanelUi.setupUi(mPanel)    
    mPanelUi.pushButton.clicked.connect(showQPanel)
    mPanelUi.pushButton_2.clicked.connect(showAPanel)
    mPanel.show()
    
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = ui_login.Ui_Login()
    ui.setupUi(Dialog)
    login = signBaidu()
    ui.pushButton.clicked.connect(zLogin)
    Dialog.show()
    mPanel = QDialog()  
    qPanel = QDialog()  
    qPanelUi = ui_question.Ui_Question()
    aPanel = QDialog()
    aPanelui = ui_answer.Ui_Answer()
    
    sys.exit(app.exec_())    
