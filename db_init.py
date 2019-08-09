from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a0e62fd88b4fe832e296132678dcae41'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:helloworld101@localhost:5432/hestavesta'
db = SQLAlchemy(app)
