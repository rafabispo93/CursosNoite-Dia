# views.py
import json
from flask import render_template, request

from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/adicionarCurso', methods=['POST'])
def add_curso():
    request_data = json.loads(request.data.decode("utf-8"))
    print("request_data", request_data)
    for key in request_data:
        print(request_data[key])
    return json.dumps(request_data), 200
