from flask import Flask, render_template, request
import json

app = Flask('MyApp')


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/signup', methods=['POST'])
def sign_up():
    form_data = request.form
    return render_template('thankyou.html', data=form_data)


@app.route('/select-language')
def select_language():
    return render_template('select-language.html')


@app.route('/language-details', methods=['POST'])
def get_language_details():
    data = json.load(open('static/js/data.json'))
    language = request.form['language']
    language_data = data[language]
    return render_template('language-details.html', data=language_data)


app.run(debug=True)
