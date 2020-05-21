from flask import Flask
from flask_restful import Resource, Api

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

# @app.route("/") 
# def home_view(): 
#         return "<h1>Welcome to Geeks for Geeks</h1> ${}".format(items)



class ItemList(Resource):
    def get(self):
        return {"items": items}

    


api.add_resource(ItemList, '/')

if __name__ == '__main__':
    app.run()