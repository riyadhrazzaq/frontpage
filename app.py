from flask import Flask, render_template
import os, sys
import json


app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route("/")
def home():
    all_projects = []
    path = 'assets/content/'
    for item in os.listdir(path):
        file = open(path+item)
        project = json.load(file)

        tmp = {}
        for i in app.config['PROJECT_PROPERTIES']:
            if project.get(i) is not None:
                tmp[i] = project[i]
        all_projects.append(tmp)
    return render_template('main.html',dictionary=all_projects)


if __name__ == '__main__':
    app.run(debug=True)