from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_file('config.py')
db = SQLAlchemy(app=app)
