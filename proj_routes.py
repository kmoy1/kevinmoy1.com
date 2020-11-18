from app import app, render_template, request
from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import Length, Email, Required

# class Config(object):
#     SECRET_KEY = '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'

# class SolverInputForm(Form):
#     essay_question = TextField("")
#     submit = SubmitField('Submit')

#Calculator app. 
@app.route('/projects/calc_js')
def calc_js():
    return render_template('/projects/calc/calc_js.html')

@app.route('/projects/eq_solver', methods=['GET', 'POST'])
def eq_solver():
    # form = SolverInputForm(request.form)
    # if not form.validate_on_submit():
    #     return render_template('/projects/eq_solver.html', form=form)
    # if request.method == 'POST':
    #     return 'Submitted!'
    return render_template('/projects/eq_solver.html')

# @app.route('/projects/eq_solver', methods=['POST'])
# def eq_solve():
#     pass