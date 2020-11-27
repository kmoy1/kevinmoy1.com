from app import app, render_template, request
from flask import Flask, request, render_template


@app.route('/test')
def test():
   return render_template('test.html')