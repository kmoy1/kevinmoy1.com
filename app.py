from flask import Flask, render_template, request, jsonify
import re

class Config(object):
    SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

#Routes Used
import proj_routes
import notes_routes
import prob_routes
import test_routes
# from routes import *

@app.route('/')
def welcome():
    return render_template('base.html')

@app.route('/projects')
def projects_index():
    return render_template('/projects/projects_index.html')

@app.route('/notes')
def notes_index():
    return render_template('/notes/note_types.html')

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