from flask import Flask, render_template, request, redirect, url_for, flash
# Flask import for flask project us
# render_template use to render html
# request use for form submit data get
# redirect use for after form submission redirect to another page
# url_for use for redirect another page route uri pass
# flash use for flash message show

app = Flask(__name__)

app.secret_key = 'khsdfkjwehoifhsf'
# secret key use for flash messages

@app.route('/')
def home():
    name = 'Deepak'
    age = 17
    return render_template('index.html', uname=name, age=age)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # save
    flash('Form Submit Successfully....')
    return redirect(url_for('success'))

if __name__ == '__main__':
    app.run(debug=True)