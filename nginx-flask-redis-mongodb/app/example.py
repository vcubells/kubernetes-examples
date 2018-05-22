from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from models import sessions
from datetime import datetime
from models import notes
from bson import ObjectId


app = FlaskAPI(__name__)

@app.route('/active_sessions', methods=['GET'])
def active_sessions():
    redis = sessions.Sessions()
    dbsize = redis.get_active_sessions()

    return jsonify({"Sesiones activas: ": dbsize})


@app.route("/", methods=['GET', 'POST'])
def list():
    redis = sessions.Sessions()
    redis.add(datetime.now())

    mongodb = notes.Notes()

    if request.method == 'POST':
        note = request.data

        result = mongodb.create(note)

        # Se adicionó para poder manejar ObjectID
        note['_id'] = str(note['_id'])

        return note, status.HTTP_201_CREATED

    return mongodb.find()


@app.route("/<string:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):

    mongodb = notes.Notes()

    if request.method == 'PUT':
        note = request.data
        mongodb.update(key, note)
        return note

    elif request.method == 'DELETE':
        mongodb.delete(key)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    note =  mongodb.findOne(key)
    if not note:
        raise exceptions.NotFound()
    else:
        return note

    return jsonify(key)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
