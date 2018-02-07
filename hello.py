from flask import Flask, render_template, request

app = Flask('MyApp')


@app.route('/')
def hello():
    return 'Hello Flask! You\'re awesome!!!'


@app.route('/<name>')
def hello_someone(name):
    return render_template('hello.html', name=name.title())


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/signup', methods=['POST'])
def sign_up():
    form_data = request.form
    return render_template('thankyou.html', data=form_data)


app.run(debug=True)
