from flask import render_template, url_for, flash, redirect
from flask_bcrypt import Bcrypt
from form import RegistrationForm, LoginForm
from classes import Student, School
from db_init import app, db

bcrypt = Bcrypt(app)

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

    flash(f'Grade = {form.grade.data}')
    if form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(f'Grade = {form.grade.data}')
        #flash(f'School = {form.school.data}')
        #student = Student(first_name=form.first_name.data, last_name=form.last_name.data, grade=form.grade.data, school_id=form.school.data, username=form.username.data, password=encrypted_password)
        #db.session.add(student)
        #db.session.commit()
        flash(f'Hello {form.username.data}, your account has been created!', 'success')
        return redirect(url_for('login'))
    else:
        form.school.choices = [(str(school.school_id).encode("utf-8").decode("utf-8"), str(school.name).encode("utf-8").decode("utf-8")) for school in db.session.query(School).all()]

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
