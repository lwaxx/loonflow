"""
Django settings for abs project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import platform


VERSION = 'v1.0.12'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm$*&&u*9+-$g^b9lj0)**1$0$wfh1wk$ye^4p+s)cera)g3fml'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
    'apps.ticket',
    'apps.workflow',
]


ROOT_URLCONF = 'loonflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'loonflow.contexts.global_variables',
            ],
        'libraries':{
                    'loonflow_filter': 'apps.manage.templatetags.loonflow_filter',

                    }
        },
    },
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    #     ("css", os.path.join(STATIC_ROOT,'css')),


    ("bower_components", os.path.join(STATIC_ROOT, 'bower_components')),
    ("dist", os.path.join(STATIC_ROOT, 'dist')),
    ("plugins", os.path.join(STATIC_ROOT, 'plugins')),



    # ("js", os.path.join(STATIC_ROOT, 'js')),
    # ("image", os.path.join(STATIC_ROOT, 'image')),
    # ("css", os.path.join(STATIC_ROOT, 'css')),
    # ("dist", os.path.join(STATIC_ROOT, 'dist')),
    # ("plugins", os.path.join(STATIC_ROOT, 'plugins')),
    # ("fonts", os.path.join(STATIC_ROOT, 'fonts')),
    # ("font-awesome", os.path.join(STATIC_ROOT, 'font-awesome')),
    # ("img", os.path.join(STATIC_ROOT, 'img')),
    # ("bootstrap", os.path.join(STATIC_ROOT, 'bootstrap')),
    # ("apps/ueditor", os.path.join(STATIC_ROOT, 'ueditor')),
    # ("echarts", os.path.join(STATIC_ROOT, 'echarts')),
    # ("ueditor", os.path.join(STATIC_ROOT, 'ueditor')),
    # ("ventor", os.path.join(STATIC_ROOT, 'ventor')),
)

WSGI_APPLICATION = 'loonflow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

# USE_L10N = True
USE_L10N = False

USE_TZ = False

DATETIME_FORMAT = 'Y-m-d H:i:s'
TIME_FORMAT = 'H:i:s'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


LOGIN_URL = '/account/login/'
AUTH_USER_MODEL = 'account.LoonUser'

STATIC_URL = '/static/'

# this is test4
useless = ''


FIXTURE_DIRS = ['fixtures/']
STATIC_FILES_VERSION = '1.0'

LOGIN_URL = '/manage/login'

APPEND_SLASH = False  # disable urls.W002 warning

if platform.system() == 'Windows':
    HOMEPATH = os.environ['HOMEPATH']
else:
    HOMEPATH = os.environ['HOME']


# this is test5
useless1 = ""