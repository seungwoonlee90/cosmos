import os
import sys
import webbrowser
import pandas as pd
import requests
from flask import Flask, request, render_template

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)

else:
    app = Flask(__name__)

@app.route('/', methods=['POST'])
def start():
    if request.method == 'POST':
        file = request.files['file']
        if file != '':
            try :
                df = pd.read_csv(file, encoding='cp949')
                print('cp949')
            except :
                df = pd.read_csv(file)
                print('utf-8')
            
            df = df.describe(include='all')
            columns = df.columns.to_list()
            myList = df.values.tolist()

    return render_template('result.html', columns=columns, myList=myList)

@app.route('/')
def main():
    value = "hello world!"
    key = app.config.from_pyfile('config.py')
    url = f'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getCtyCodeList?serviceKey={key}' #test용 공공데이터 url
    print(requests.get(url))

    return render_template('index.html', value=value)

port = 9000
             
if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:'+str(port)+'/')
    app.run(port=port, debug=True, use_reloader=False)