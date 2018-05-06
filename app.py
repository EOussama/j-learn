from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print('...')
    if os.path.exists('data/info.json'):

        info = json.load(open('data/info.json', encoding="utf8"))
        print('Info', info)
    else:
        open('data/info.json', 'w')

    app.run(debug=True)