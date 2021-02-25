from app import app, render_template
from flask import redirect, url_for
import os
from flask_misaka import Misaka, markdown
from flask import Flask, render_template, request
Misaka(app)

def filenameFormat(filename):
    f = filename.replace("_", " ")
    f = f.replace(".pdf", "")
    f = f.replace("-", ":")
    return f

# Note index L2: By subject (LATEX)
@app.route('/notes/notes-lt')
def latexnotes_subject_index():
    routes = []
    subject_names = ["CS61B: Data Structures", "CS61C: Machine Architectures"]
    for subject in os.listdir("static/notes-lt"):
        routes.append("/notes/notes-lt/" + subject)
    return render_template('/notes/notes_subject_index.html', len = len(subject_names), subjects=subject_names, routes=routes)

#Note index L2: By subject (MARKDOWN)
@app.route('/notes/notes-md')
def mdnotes_subject_index():
    sub_lst = []
    static_paths = []
    for subject in os.listdir("static/notes-md"):
        sub_lst.append(subject)
        static_paths.append("/notes/notes-md/" + subject)
    return render_template('/notes/notes_subject_index.html', len = len(sub_lst), subjects=sub_lst, routes=static_paths)

#Note index L3: By note (given subject) (LATEX)
#Note filename MUST be in format Note_{note number}-_{title}
@app.route('/notes/notes-lt/<subject>')
def latexnotes_note_index(subject):
    note_names = []
    note_filepaths = []
    notes_lst = os.listdir("static/notes-lt/" + subject)
    notes_lst.sort(key = lambda x: float(x.split('_')[1].replace('-','')))
    for note in notes_lst:
        note_names.append(filenameFormat(note))
        note_filepaths.append(note)
    return render_template('/notes/notes_note_index.html', subject=subject, N=len(note_names), notes_lst = note_names, note_filenames = note_filepaths, latex="True")

#Note index L3: By note (given subject) (MARKDOWN)
@app.route('/notes/notes-md/<path:path>')
def md_indexer(path):
    problems_lst = []
    if os.path.isdir("static/problems/" + path):
        for note in os.listdir("static/problems/" + path):
            problems_lst.append(note)
        return render_template('/problems/problems_index.html', subject=path, N=len(problems_lst), problems_lst = problems_lst)
    else: #Path
        filename = "static/notes-md/" + path
        md_file = open(filename, "r").read()
        return render_template('test.html', md_file = markdown(md_file, fenced_code=True, math=True, math_explicit=True))



