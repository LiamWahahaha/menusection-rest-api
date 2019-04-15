import os
from flask import Flask
from flask_restful import Api
from resources.menusection import Menusection, MenusectionList
from utils.flaskrun import flaskrun

app = Flask(__name__)
app.config['DEBUG'] =  True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///menusection.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)
api = Api(app)
api.add_resource(Menusection, '/menusection/<int:id>')
api.add_resource(MenusectionList, '/menusection')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    flaskrun(app)
