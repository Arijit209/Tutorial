from flask import Flask
app = Flask(__name__)

@app.route('/') # Basic Route
def home():
    return 'Home Page'

@app.route('/about') # Multiple Route
def about():
    return 'About page'

if __name__ == '__main__':
    app.run(debug=True)