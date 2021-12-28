from pathlib import Path


SECRET_KEY = 'django-insecure-)ev2$(@&d2%imw-08dwhd&!9bl1i4a=sd5ahek$ylp+y3c)ns&'


BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
