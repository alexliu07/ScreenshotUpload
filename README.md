# 自动屏幕截图及上传工具
#### 此软件可以自动隔一段时间给屏幕截图，并且可以在需要的时候自动上传给对应的服务端。
***
## 软件特点
***
* 客户端可以进行后台屏幕截图
* 支持手动设置截图间隔时间
* 支持远程上传屏幕截图到指定服务器
* 支持保存屏幕截图到本地
* 服务端支持分设备保存截图
***
## 使用方法
***
#### 此软件分为服务端和客户端，服务端
***
***提示：无论是服务端或者客户端，请勿放置在系统目录之类的没有普通权限的目录，否则将会报错***<br>
***本程序仅供学习和研究Python中的截屏和图片的上传功能使用，请勿用于其他用途***
***
### 服务端使用
1. Python服务端的使用
    - 首先需安装Flask库
    - 接着使用Python3运行server.py就可以了
2. Windows客户端的使用
    - 直接解压后运行server.exe并允许通过防火墙即可
***
### 客户端使用
客户端有两种使用方式，分别为set（设定）模式和run（运行）模式

设定模式会弹出一个窗口，可在里面设置服务状态、服务器地址、间隔时间和保存到本地

运行模式将不会有任何提示
1. Python版本使用
    - 首先安装pyautogui,pillow,requests库
    - 运行模式建议使用pythonw运行（隐藏窗口）<br>
    设定模式：
    `pythonw client.py set`<br>
    运行模式：
    `pythonw client.py run`
    <br>
2. Windows版本使用
    <br>
    `client set`（设定模式）
    <br>
    `client run`（运行模式）
