from app import app, render_template
import os

@app.route('/notes/<subject>')
def notes_subject_index(subject):
    notes_lst = []
    for note in os.listdir("static/notes/" + subject):
        notes_lst.append(note)
    notes_lst.sort()
    return render_template('/notes/notes_index2.html', subject=subject, N=len(notes_lst), notes_lst = notes_lst)

