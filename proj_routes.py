from app import app, render_template

#Calculator app. 
@app.route('/projects/calc_js')
def calc_js():
    return render_template('/projects/calc/calc_js.html')

