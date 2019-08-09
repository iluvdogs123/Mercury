from db_init import db


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), unique=False, nullable=False)
    last_name = db.Column(db.String(32), unique=False, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.school_id'), nullable=False)

    def __repr__(self):
        return f"Student'({self.username}','{self.image_file}')"


class School(db.Model):
    school_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True )
    zipcode = db.Column(db.String(10), nullable=False, unique=True)
    city = db.Column(db.String(35), nullable=False, unique=True)
    state = db.Column(db.String(20), nullable=False, unique=True)
    number_of_students = db.Column(db.Integer)
    school = db.relationship("Student", backref="school", lazy=True)

    def __repr__(self):
        return f"School'({self.name}')"
