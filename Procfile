web: python manage.py runserver 0.0.0.0:$PORT
heroku buildpacks:clear
heroku buildpacks:add --index heroku/python
heroku ps:scale web=1
