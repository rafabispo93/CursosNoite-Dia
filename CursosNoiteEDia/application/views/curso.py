import json

from flask import Blueprint, render_template, request

mod_curso = Blueprint('mod_curso', __name__)


@mod_curso.route('/adicionarCurso', methods=['POST'])
def add_curso():
    request_data = json.loads(request.data.decode("utf-8"))
    print("request_data", request_data)
    for key in request_data:
        print(key, request_data[key])
    return json.dumps(request_data), 200
