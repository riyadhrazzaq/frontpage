from flask import Flask, render_template
import os, sys
import json


app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route("/")
def home():
    """
    Variables
    ---------
    contents: dict of dicts. Each dict is a folder in 'content/'
    """
    
    base = os.path.abspath(os.getcwd())+'/'
    path = base+app.config['CONTENT_PATH']
    section_config = app.config['SECTIONS']
    
    contents = []
    for section in section_config:

        section_path = path+section['heading']+'/'

        level_one = {}
        level_one['heading'] = section['heading']
        level_one['data'] = []
        for item in os.listdir(section_path):
            file = open(section_path+item)
            target = json.load(file)

            level_one['data'].append(target)

        contents.append(level_one)
        
    return render_template('main.html',contents=contents)


if __name__ == '__main__':
    app.run(debug=True)
