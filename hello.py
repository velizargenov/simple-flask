from flask import Flask, render_template, request

app = Flask('MyApp')


@app.route('/')
def hello():
    return 'Hello Flask! You\'re awesome!!!'


@app.route('/<name>')
def hello_someone(name):
    return render_template('hello.html', name=name.title())


def asd():
    return 'hi'


app.run(debug=True)
