from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
info = []

@app.route('/')
def index():
    return render_template('index.html', info = info)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/edit/<string:jap>/')
def edit(jap):
    term = {}

    for _ in info:
        if _['Japanese'] == jap:
            term = _
            break

    return render_template('edit.html', jap = term)

@app.route('/add/data/', methods = ['post'])
def sendData():
    json_data = json.loads(request.form['json_data'])
    list.append(info, json_data)

    with open('data/info.json', 'w') as file:
        json.dump(info, file)

    return json_data['Japanese']

@app.route('/edit/data/', methods = ['POST'])
def sendEdit():
    json_data = json.loads(request.form['json_data'])
    oldTerm = json.loads(request.form['oldTerm'])

    for i in range(0, len(info)):
        if info[i] == oldTerm:
            info[i] = json_data
            break

    with open('data/info.json', 'w') as file:
        json.dump(info, file)

    return oldTerm['Japanese']

@app.route('/delete/', methods = ['POST'])
def deleteTerm():
    data = request.form['index']
    
    try:
        del info[int(data)]

        with open('data/info.json', 'w') as file:
            json.dump(info, file)
    except:
        print('[Error]: Something went wrong!')

    return data

if __name__ == '__main__':
    if os.path.exists('data/info.json'):
        with open('data/info.json') as file:
            info = json.load(file)
    else:
        open('data/info.json', 'w')

    app.run()