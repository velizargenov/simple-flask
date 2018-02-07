from flask import Flask

app = Flask('MyApp')


@app.route('/')
def hello():
    return 'Hello Flask! You\'re awesome!!!'


app.run(debug=True)
