from app import app, render_template

@app.route('/test2', methods=['GET'])
def test2():
    return render_template('test2.html')