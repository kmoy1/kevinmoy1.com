from app import app, render_template, request

#Calculator app. 
@app.route('/projects/calc_js')
def calc_js():
    return render_template('/projects/calc/calc_js.html')

@app.route('/projects/eq_solver')
def eq_solver():
    return render_template('/projects/eq_solver.html')

@app.route('/projects/eq_solver', methods=['POST'])
def eq_solve():
    pass