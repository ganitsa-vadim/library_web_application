flask db init
flask db migrate
flask db upgrade
gunicorn --bind 0.0.0.0:5000 -w 3 run:app