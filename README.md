frastPyqt
=========

基于百度知道的GUI小脚本
使用库
pyqt
PyQuery




环境win7 64 bit

使用pyinstaller打包python为exe文件


1、下载pyinstaller

目前pyinstaller支持的python版本为2.3-2.7,可以到http://www.pyinstaller.org/官网下载。

2、安装

下载完成后，解压即可。

3、pyinstaller使用方法

使用也非常的简单，cmd下进入解压出来的目录，执行如下命令。

python pyinstaller.py [opts] yourprogram.py
主要选项包括：

-F, –onefile 打包成一个exe文件。
-D, –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）。
-c, –console, –nowindowed 使用控制台，无界面(默认)
-w, –windowed, –noconsole 使用窗口，无控制台
