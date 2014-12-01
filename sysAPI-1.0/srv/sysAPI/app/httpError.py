from flask import jsonify


def httperror(error, description, code):
    return jsonify({'error': error, 'description': description}), code