from flask import Flask
from flask_restful import Resource, Api
import mysql.connector

config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'port': '3306',
    'database': 'items'
}


app = Flask(__name__)
api = Api(app)

items = [
    {
        'name': 'Lam',
        'grade': 10
    },
    {
        'name': 'Tester',
        'grade': 3
    }
]

class ItemList(Resource):
    def get(self):
        return items

    # def post(self):
    #     connection = mysql.connector.connect(**config)
    #     cursor = connection.cursor()
    #     cursor.execute('SELECT * FROM items')
    #     results = [{name: item} for (name, grade) in cursor]
    #     cursor.close()
    #     connection.close()


api.add_resource(ItemList, '/')

if __name__ == '__main__':
    app.run(port=4999, debug=True)