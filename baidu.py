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
from PyQt4 import QtGui
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
        resp = urllib2.urlopen(req)
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
            #print self.requestData
            self.result = self.getLoginRequest()
            if self.result == '0':
                postData = urllib.urlencode(self.postDict)
                self.getURL(self.loginUrl, postData)
                self.result = self.getLoginRequest()
            elif self.result == '1':
                print 'Login FAIL!'
        else:
            print 'Construct Post data fail.'

    def getLoginRequest(self):
        """Get infomation from login page"""
        #print 'in getLoginRequest'
        if "请您输入验证码" in self.requestData:
            d=pq(self.requestData)
            vcodeimgUrl=d('.row-padbtm-10').find('img').attr('src')
            self.vcodestr = vcodeimgUrl.split('?')[1]
            print '-' * 79
            #print vcodeimgUrl
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(urllib.urlopen(vcodeimgUrl).read())
            ui.vcodeImg.setPixmap(pixmap)
            #urllib.urlretrieve(vcodeimgUrl,'test.jpg')  
            print '-' * 79
            #self.vcode = raw_input('Verification code:')
            self.postDict['vcodestr'] = self.vcodestr
            #self.postDict['verifycode'] = self.vcode
            #print self.postDict
            return '0'
        elif "您输入的密码有误" in self.requestData:
            print 'Password WRONG!'
            #print self.requestData
            self.getLoginRequest()
            #return '1'

        elif "您输入的验证码有误" in self.requestData:
            print 'Verifycode WRONG!'
            #print self.requestData
            return '1'

        elif "系统错误" in self.requestData:
            print 'Unexpect Error!'
            #print self.requestData
            self.getLoginRequest()
            #return '1'

        else:
            for line in self.requestData.split('<'):
                if 'itj=23' in line:
                    self.tbUrl = line.split('"')[1].replace('amp;', '')
                    print 'Get Baidu Bar Url...Success!'
            #print self.requestData

    def getBar(self):
        """Get Baidu Bar List"""
        #print 'in getBar'
        favoUrl = ''
        self.getURL(self.tbUrl, None)
        #print self.requestData
        for line in self.requestData.split('<'):
            if 'tab=favorite' in line:
                favoUrl = self.mainUrl + line.split('"')[1]
                break

        if favoUrl:
            self.getURL(favoUrl, None)
            #print self.requestData
            for line in self.requestData.split('<'):
                if 'm?kw' in line:
                    tmp_tbUrl = favoUrl.split('?')[0] + "?" + line.split('"')[1].split('?')[1]
                    self.barlist.append(tmp_tbUrl.replace('amp;', ''))
                    #print tmp_tbUrl.replace('amp;', '')

    def signBar(self):
        """Sign in Baidu Bar"""
        #print 'in signBar'
        if self.checkBar():
            print 'OK!'
            print '-' * 40
            print 'Baidu Bar Sign starting...'
            for url in self.barlist:
                self.getURL(url, None)
                for line in self.requestData.split('<'):
                    if 'sign?' in line:
                        self.getURL(self.mainUrl + line.split('"')[1].replace('amp;',''),None)
                        break
                for i in range(len(self.requestData.split('/'))):
                    if 'name="top"' in self.requestData.split('/')[i]:
                        temp_info = self.requestData.split('/')[i + 1]
                        break
                if '签到成功' in temp_info:
                    print 'Success:',urllib.unquote(url.split('=')[1]).decode('utf8'),\
                                     temp_info.split('>')[2].split('<')[0].decode('utf8') +\
                                     temp_info.split('>')[3].strip('<').decode('utf8')
                else:
                    print 'Fail:',urllib.unquote(url.split('=')[1]).decode('utf8')
                    self.faillist.append(url)
            print '-' * 40
        else:
            print 'Fail:No favourite bar.'

    def showBarName(self, bar_list):
        """Show Bar Name"""
        #print 'in showBarName'
        print '-' * 40
        for url in bar_list:
            print urllib.unquote(url.split('=')[1]).decode('utf8')
        print '-' * 40

    def checkBar(self):
        """Check Bar list"""
        #print 'in checkBar'
        if self.barlist:
            return True
        else:
            return False

    #--------------------------------------------------------------------------------
    def getURL_threading(self, url, data):
        """Open webpages and get the HTML code by each threading"""
        #print 'in getURL'
        req = urllib2.Request(url, data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        resp = urllib2.urlopen(req)
        #print 'Get Url:', url
        return resp.read()

    def signBar_threading(self, barUrl):
        """Sign in Baidu Bar by using threading"""
        resp = self.getURL_threading(barUrl, None)
        for line in resp.split('<'):
            if 'sign?' in line:
                #print self.mainUrl + line.split('"')[1].replace('amp;','')
                resp = self.getURL_threading(self.mainUrl + line.split('"')[1].replace('amp;',''),None)
                break

        for i in range(len(resp.split('/'))):
            if 'name="top"' in resp.split('/')[i]:
                temp_info = resp.split('/')[i + 1]
                break
        if '签到成功' in temp_info:
            print 'Success:',urllib.unquote(barUrl.split('=')[1]).decode('utf8'),\
                             temp_info.split('>')[2].split('<')[0].decode('utf8') +\
                             temp_info.split('>')[3].strip('<').decode('utf8')
        else:
            print 'Fail:', urllib.unquote(barUrl.split('=')[1]).decode('utf8')
            self.faillist.append(barUrl)

    def sign_threading(self):
        worker = []
        names = locals()
        print 'OK!'
        print '-' * 40
        print 'Baidu Bar Sign starting...'
        for i in range(0,len(self.barlist)):
            names['t%d' % i]  = threading.Thread(target=self.signBar_threading,args=(self.barlist[i],))
            names['t%d' % i].start()
            worker.append(names['t%d' % i])
            if i % 5 == 0 and i > 0:
                print 'Thread-' + str(i / 5) + ' Starting...'
                for row in worker:
                    row.join()
                worker = []
    def answer(self,url,postDict):
        postData = urllib.urlencode(postDict)
        self.getURL(url, postData)
        print self.requestData 
        if "提交" in self.requestData:
            d=pq(self.requestData)
            vcodeimgUrl=d('.vcode-img').attr('src')
            tpixmap = QtGui.QPixmap()
            tpixmap.loadFromData(urllib.urlopen(vcodeimgUrl).read())

            aPanelui.vcodeimg.setPixmap(tpixmap)

            self.answerPost['vcodestr'] = vcodeimgUrl.split('?')[1]
            self.answerPost['vcodestr'] = re.findall(r"codestr=(.*)",postDict['vcodestr'])[0]


            

    def question(self,title,content,vcode):
        self.questionPost['vcode'] = vcode
        self.questionPost['score'] = 0
        self.questionPost['anonymous'] = 0
        self.questionPost['title'] = title
        self.questionPost['content'] = content
        postData = urllib.urlencode(self.questionPost)
        self.getURL('http://zhidao.baidu.com/msubmit/ask?ta=1&amp;pu=null&amp;cifr=null', postData)
        print self.requestData 
        if "输入验证码" in self.requestData: 
            d=pq(self.requestData)
            vcodeimgUrl=d('.vcode-img').attr('src')
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(urllib.urlopen(vcodeimgUrl).read())
            qPanelUi.vcodeimg.setPixmap(pixmap)
            #vcode = raw_input('Verification code:')   
            self.questionPost['vcodestr'] = vcodeimgUrl.split('?')[1]
            self.questionPost['vcodestr'] = re.findall(r"codestr=(.*)",self.questionPost['vcodestr'])[0] 
            #postDict['vcode']=vcode
            #print postDict
            #postData = urllib.urlencode(postDict)  
            #self.getURL('http://zhidao.baidu.com/msubmit/ask?ta=1&amp;pu=null&amp;cifr=null', postData)        
            
    #--------------------------------------------------------------------------------

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
    login.question(title,content,vcode)
    
def sinAnswer(): 
    url='http://zhidao.baidu.com/msubmit/submitedit?cifr=null&step=2&ref_name=answer&svf=wap_reply'


    login.answerPost['qid'] = str(aPanelui.qid.text().toUtf8())
    login.answerPost['content'] = str(aPanelui.content.toPlainText().toUtf8())
    login.answerPost['vcode'] = str(aPanelui.vcode.text().toUtf8())
    if login.answerPost['vcode']:
        url='http://zhidao.baidu.com/msubmit/answer?ta=1&cifr=null'
    print login.answerPost
    login.answer(url, login.answerPost)

def zLogin():
    login.username = str(ui.userName.text().toUtf8())
    login.password = str(ui.password.text().toUtf8())
    login.postDict['vcode'] = str(ui.vcode.text().toUtf8())
    login.postDict['verifycode'] = login.postDict['vcode']
    main()

def main():   
    login.loginBaidu()
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
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = ui_login.Ui_Login()
    ui.setupUi(Dialog)
    login = signBaidu()
    ui.pushButton.clicked.connect(zLogin)
    Dialog.show()
    mPanel = QtGui.QDialog()  
    qPanel = QtGui.QDialog()  
    qPanelUi = ui_question.Ui_Question()
    aPanel = QtGui.QDialog()
    aPanelui = ui_answer.Ui_Answer()
    
    sys.exit(app.exec_())    
