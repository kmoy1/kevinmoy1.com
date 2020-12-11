from flask_misaka import Misaka, markdown
from flask import Flask, render_template, request
# from flaskext.markdown import Markdown
from app import app, render_template, request

Misaka(app)

@app.route('/test')
def test():
   md_file = open("static/notes-md/test.md", "r").read()
   return render_template('test.html', md_file = markdown(md_file, fenced_code=True, math=True, math_explicit=True))

