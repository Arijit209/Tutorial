from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from werkzeug.security import generate_password_hash
from db.db_connect import get_connection

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kjsfhskdfjsdkf'

class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=10)]
    )

    email = EmailField(
        'Email',
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6)]
    )

    confirm = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=10)]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6)]
    )

    submit = SubmitField('Login')

@app.route('/home')
def home():
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(
                '''
                    CREATE TABLE IF NOT EXISTS students(
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) UNIQUE NOT NULL,
                        city VARCHAR(50),
                        password VARCHAR(255) NOT NULL
                    )
                '''
            )
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            return f'Error : {e}'
    else:
        return 'Failed to connect'
    return 'Home'
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        # Hash password
        password = generate_password_hash(form.password.data)
        conn = get_connection()
        if conn:
            try:
                cur = conn.cursor()
                query = '''
                    INSERT INTO students(
                        name,
                        email,
                        password
                    ) VALUES (%s, %s, %s)
                '''
                cur.execute(query, (username, email, password))
                conn.commit()
                cur.close()
                conn.close()
                return 'Registration Successful'
            except Exception as e:
                return render_template(
                    'register.html',
                    form=form,
                    error=str(e)
                )

        else:
            return 'Failed to connect database'

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        return f'Welcome {username}'

    return render_template('login.html', form=form)

@app.route('/users')
def user():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    query = '''
                SELECT * FROM students
            '''
    cur.execute(query)
    usersdata = cur.fetchall()
    return render_template('usersdata.html', users_data=usersdata)

if __name__ == '__main__':
    app.run(debug=True)