from flask import Flask, url_for, redirect, abort
from flask.cli import main

print('begin new Flask __name__ = %s --my' % __name__)
app = Flask(__name__)
print('finish Flash --my')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    '''
    可以通过这个启动debug模式
    '''
    url_for()
    redirect()
    abort()
    app.run(host='127.0.0.1', port=5001)