from app import app, render_template
import os

@app.route('/notes/<subject>')
def notes_subject_index(subject):
    notes_lst = []
    #TODO: Populate notes_lst with valid paths of this notes.
    return render_template('/notes/notes_index2.html', notes_lst = notes_lst)

