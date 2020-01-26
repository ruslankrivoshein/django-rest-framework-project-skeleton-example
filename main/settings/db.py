# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import environ


root = environ.Path(__file__) - 3

env = environ.Env()
environ.Env.read_env(f'{str(root)}/.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'HOST': env.str('DB_HOST'),
        'USER': env.str('DB_USER'),
        'PORT': env.str('DB_PORT'),
        'PASSWORD': env.str('DB_PASSWORD'),
    }
}
