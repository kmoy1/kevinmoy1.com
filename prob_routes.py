from app import app, render_template
from flask import redirect, url_for
import os
from flask_misaka import Misaka, markdown
from flask import Flask, render_template, request
Misaka(app)


@app.route('/problems')
def problems_root_index():
    sub_lst = []
    static_paths = []
    for subject in os.listdir("static/problems"):
        sub_lst.append(subject)
        static_paths.append("/problems/" + subject)
    return render_template('/problems/problems_subject_index.html', N = len(sub_lst), subjects=sub_lst, routes=static_paths)

@app.route('/problems/<path:path>')
def problems_indexer(path):
    problems_lst = []
    if os.path.isdir("static/problems/" + path):
        for note in os.listdir("static/problems/" + path):
            problems_lst.append(note)
        return render_template('/problems/problems_index.html', subject=path, N=len(problems_lst), problems_lst = problems_lst)
    else:
        filename = "static/problems/" + path
        md_file = open(filename, "r").read()
        return render_template('test.html', md_file = markdown(md_file, fenced_code=True, math=True, math_explicit=True))

