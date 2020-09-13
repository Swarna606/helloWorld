from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'hello world, chaitanya!!'

@app.route('/3ri')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'technologies'


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")