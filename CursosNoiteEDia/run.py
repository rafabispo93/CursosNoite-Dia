# run.py

from app import app
from models import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cursos:cursos@localhost/cursosNoiteDia'
# ...app config...
db.init_app(app)
if __name__ == '__main__':
    app.run()
    manager.run()
