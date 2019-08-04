from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a0e62fd88b4fe832e296132678dcae41'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:helloworld101@localhost:5432/hestavesta'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), unique=True, nullable=False)
    last_name = db.Column(db.String(32), unique=True, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    school_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User'({self.username}','{self.image_file}')"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        student = Student(first_name='Sharanya', last_name='Nair', grade= 8, school_id=1, username=form.username.data, password=encrypted_password )
        db.session.add(student)
        db.session.commit()
        flash(f'Hello {form.username.data}, your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',  methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'Password':
            flash(f'Welcome to HestaVesta, {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password, please try again', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
