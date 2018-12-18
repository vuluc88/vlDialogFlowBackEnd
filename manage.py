from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from examples import todo

app = Flask(__name__)
api = Api(app)

##
## setup the Api resource routing here
##
api.add_resource(todo.TodoList, '/todos')
api.add_resource(todo.Todo, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
