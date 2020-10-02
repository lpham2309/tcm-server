from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from .settings import config

app = Flask(__name__)

app.config['MYSQL_HOST'] = config['db_host']
app.config['MYSQL_USER'] = config['db_user']
app.config['MYSQL_PASSWORD'] = config['db_password']
app.config['MYSQL_DB'] = config['db_name']

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(config['db_user'], config['db_password'], config['db_host'], config['db_name'])

db = MySQL(app)

api = Api(app)
