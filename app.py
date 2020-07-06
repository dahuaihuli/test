from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/demo')
def demo():
    return '叶良辰快快出来受死'

if __name__="__main__":

    app.debug=True
    app.run()
