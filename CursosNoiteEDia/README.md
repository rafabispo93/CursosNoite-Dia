## To run the website service
   Run the file called runMe.sh
## Create the database
   - sudo -u postgres psql
   - createuser cursos -P -S -D -R
   - createdb cursosNoiteDia -O cursos
   - psql -c "GRANT ALL PRIVILEGES ON database cursosNoiteDia TO cursos"
   - python manage.py db init
   - python manage.py db migrate
   
