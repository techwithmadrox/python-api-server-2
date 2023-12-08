from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app = create a flask application
app = Flask(__name__)
print("[]Name" + __name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from app import routes