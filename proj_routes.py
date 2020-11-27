from app import app, render_template, request
import string
# from project_code import eq_solve
import numpy as np
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.solvers import solve
from sympy import Symbol, solveset, degree, latex, simplify

@app.route('/projects/calc_js')
def calc_js():
    return render_template('/projects/calc/calc_js.html')

@app.route('/projects/eq_solver')
def eq_solver():
    #Generate solutions here. 
    eq_str = request.args.get('eq', 0)
    if not eq_str:
        return render_template('/projects/eq_solver.html')

    #Simplify expression (if necessary)
    sympy_eq_str = eq_str.replace('^', '**')
    try:
        simplified_expr = str(simplify(sympy_eq_str)).replace('**', '^')
    except:
        simplified_expr = eq_str
    #Calculate zeros + complex solutions
    expr = parse_expr(sympy_eq_str, transformations=(standard_transformations + (implicit_multiplication_application,)))
    try:
        simplified_expr = str(simplify(expr)).replace('**', '^').replace('*','')
    except:
        simplified_expr = eq_str
    sols = list(solveset(expr, Symbol('x')))
    complex_sols = [complex(sol) for sol in sols if not sol.is_real]
    sols = [float(sol) for sol in sols if sol.is_real]
    return render_template('/projects/eq_solver.html', zeros = sols, complex_sols = complex_sols, eq = simplified_expr, submit="Yes")
