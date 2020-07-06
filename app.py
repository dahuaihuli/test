from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello 龙傲天'

if __name__="__main__":

    app.debug=True
    app.run()
