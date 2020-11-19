from app import app, render_template, request
from project_code import eq_solve
import numpy as np
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
    if request.method == 'POST':
        #Generate solutions here. 
        eq_str = request.form['eq']
        sols = eq_solve.solve(eq_str)
        return render_template('/projects/eq_solver.html', eq = eq_str, submit="Yes")
    else:
        return render_template('/projects/eq_solver.html')
