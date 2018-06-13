from flask import Flask, render_template, abort
import os
import JSON

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/files/<filename>')
def file(filename):
    path = '/home/shiyanlou/files/'
    if os.path.exists(path +filename+'.json'):
        return render_template(JSON.stringify(path+filename+'.json'))
    else:
        return render_template('404.html')

