"""UserSrv
Usage:
    UserSrv.py --port=<int>
Options:
    -h --help     Show this screen.
    --port=<int>  port used
"""

# To run the server
# flask --app user_server run --port=8888

import logging
from docopt import docopt
from flask import Flask, Response, request, jsonify
from flask_json_schema import JsonSchema, JsonValidationError
import functions_db as db

APP = Flask(__name__)
SCHEMA = JsonSchema(APP)


@APP.errorhandler(JsonValidationError)
def validation_error(json_error):
    error = { \
        'error': json_error.message, \
        'errors': [validation_error.message for validation_error in json_error.errors] \
    }
    return jsonify(error), 400

@APP.route('/isalive', methods=['GET'])
def is_alive():
    return Response(status=200)

# of course schemas shall go in a separated folder
LOGIN_SCHEMA = { \
    "type" : "object", \
    "required" : ["username", "password"], \
    "properties" : { \
        "username" : {"type" : "string"}, \
        "password" : {"type" : "string"}, \
    }, \
}
@APP.route('/login', methods=['POST'])
@SCHEMA.validate(LOGIN_SCHEMA)
def login():
    json_payload = request.json
    if json_payload is not None:
        db.add_user(json_payload['username'], json_payload['password'])

        return Response(status=200)
    return Response(status=400)

TEXT_SCHEMA_PUBLIC = { \
    "type" : "object", \
    "required" : ["id"], \
    "properties" : { \
        # "username" : {"type" : "string"}, \
        # "password" : {"type" : "string"}, \
        "id" : {"type" : "integer"}, \
    }, \
}
@APP.route('/get_text_public', methods=['GET'])
@SCHEMA.validate(TEXT_SCHEMA_PUBLIC)
def get_text_public():
    json_payload = request.json
    if json_payload is not None:
        res = db.get_text(json_payload['id'])
        return res
    return Response(status=400)

TEXT_SCHEMA_PRIVATE = { \
    "type" : "object", \
    "required" : ["id"], \
    "properties" : { \
        "username" : {"type" : "string"}, \
        "password" : {"type" : "string"}, \
        "id" : {"type" : "integer"}, \
    }, \
}
@APP.route('/get_text_private', methods=['GET'])
@SCHEMA.validate(TEXT_SCHEMA_PRIVATE)
def get_text_private():
    json_payload = request.json
    if json_payload is not None:
        if (not(db.valid_user(json_payload['username'], json_payload['password']))):
            return "Bad username"
        res = db.get_text(json_payload['id'])
        return res
    return Response(status=400)

@APP.route('/historique_texte',methods=['GET'])
@SCHEMA.validate(LOGIN_SCHEMA)
def historique_texte():
    json_payload = request.json
    if json_payload is not None:
        texts = db.get_texts_user(json_payload['username'],json_payload['password'])
        return texts
    return Response(status=400)

if __name__ == '__main__':
    ARGS = docopt(__doc__)
    if ARGS['--port']:
        APP.run(host='localhost', port=ARGS['--port'])
    else:
        logging.error("Wrong command line arguments")
