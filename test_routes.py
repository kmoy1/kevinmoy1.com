from flask_misaka import Misaka, markdown
from flask import Flask, render_template, request
# from flaskext.markdown import Markdown
from app import app, render_template, request

Misaka(app)

@app.route('/test')
def test():
   return render_template('test.html')

@app.route('/mcq-test')
def mcq_test():
   return render_template('mcq.html')