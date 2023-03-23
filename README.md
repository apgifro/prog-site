# Programação III

## Dependências

```
pip install django==3.2.18
pip install dj-static django-stdimage
```

## Comandos úteis

### Iniciar
```
django-admin startproject nome .
django-admin startapp core
```

### Models

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Executar

```
python manage.py runserver
```

## Imagens

![screen1](/readme/s1.png)

![screen2](/readme/s2.png)


## Deploy no Python Anywhere

Criar runtime.txt
```
python-3.10
```

Ajustar SECRET_KEY e Debug no settings.py

```
os.environ.get('DJANGO_SECRET_KEY', ...)
os.environ.get('DJANGO_DEBUG', '') != 'False'
```

Instalar dependências
```
gunicorn==20.1.0
mysqlclient==2.1.1
```

Criar Procfile
```
web: gunicorn minhaempresa.wsgi:core --log-file -
```


Console do Python Anywhere
```
mkvirtualenv --python=/usr/bin/python3.10 venv
git clone https://github.com/apgifro/prog.git
pip install -r requirements.txt
python manage.py collectstatic
```

Criar Web App - Open Web tab

Renomear site no arquivo WSGI

Editar novamente settings.py

```
ALLOWED_HOSTS = ["apg.pythonanywhere.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'apg$default',
        'HOST': 'apg.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'USERNAME': 'apg',
        'PASSWORD': 'senha'
    }
}
```

Executar migrations
```
python manage.py makemigrations
python manage.py migrate
```

Feito!