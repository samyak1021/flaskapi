
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask import abort
import mysql.connector

# Creating connection with mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="movie_db"
)


# creating the flask app
app = Flask(__name__)
api = Api(app)


class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for the particular movie_id
    def get(self,id):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("select * from movies where id ={id}".format(id=id))
        result = cursor.fetchall()
        resp = None
        for movie in result:
            resp = movie
        if not resp:
            abort(404)
        return jsonify(resp)

    

# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/v1/movie/<int:id>')


if __name__ == '__main__':

    app.run(debug=True)
