from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)
app.config.from_object(__name__)

#Routes Used
import proj_routes
import notes_routes
import prob_routes


@app.route('/')
def welcome():
    return render_template('base.html')

@app.route('/projects')
def projects_index():
    return render_template('projects/projects_index.html')

@app.route('/notes')
def notes_index():
    import os
    sub_lst = []
    links = []
    routes = []
    for subject in os.listdir("static/notes"):
        links.append("static/notes/" + subject)
        sub_lst.append(subject)
        routes.append("/notes/" + subject)
    return render_template('/notes/notes_index.html', len = len(sub_lst), links=links, subjects=sub_lst, routes=routes)

@app.route('/problems')
def problems_index():
    return render_template('/problems/problems_index.html')

@app.route('/resume')
def resume_index():
    return render_template('resume.html')

@app.route('/about')
def aboutme_index():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(threaded=True)