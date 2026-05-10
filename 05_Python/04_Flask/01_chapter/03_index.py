from flask import Flask
app = Flask(__name__)

@app.route('/profile/')
@app.route('/profile/<name>') # Dynamic Route
def profile(name='Guest'):
    return f'This is my profile, for {name}'

@app.route('/product/<int:id>') # Type Define
def product(id):
    return f'Product Id is {id}'

if __name__ == '__main__':
    app.run(debug = True)