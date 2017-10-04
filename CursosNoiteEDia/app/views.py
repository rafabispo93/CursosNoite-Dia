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
    request_data = json.dumps(request.data.decode("utf-8"))
    print(request_data)
    return ''
