"""
Django settings for laboratorium-ee-2019 project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from django.utils.translation import gettext_lazy as _
from wagtail.core import hooks
import environ
import os


BASE_DIR = str(environ.Path(__file__) - 3)
SRC_DIR = os.path.join(BASE_DIR, 'ee_site')
env = environ.Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webpack_loader',
    'settings_context_processor',
    'captcha',

    'wagtail.admin',
    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.core',
    'wagtail.documents',
    'wagtail.embeds',
    'wagtail.images',
    'wagtail.search',
    'wagtail.sites',
    'wagtail.snippets',
    'wagtail.users',
    'wagtail_modeltranslation',
    'wagtail_modeltranslation.makemigrations',
    'wagtail_modeltranslation.migrate',
    'wagtailmenus',

    'modelcluster',
    'taggit',

    'bulma',  # for automatic form rendering

    'ee_site.apps.main',
    'ee_site.apps.projects',
    'svg'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'ee_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SRC_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'settings_context_processor.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

WSGI_APPLICATION = 'ee_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL'),
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('pl', _('Polish')),
    ('en', _('English')),
]
MODELTRANSLATION_LANGUAGES = [
    'pl',
    'en',
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = env('STATIC_ROOT', default=os.path.join(BASE_DIR, 'staticdir'))
STATICFILES_DIRS = [
    os.path.join(SRC_DIR, 'static', 'dist')
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

SVG_DIRS = [os.path.join(SRC_DIR, 'static', 'src', 'images')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediadir')
MEDIA_URL = '/media/'

# GOOGLE ANALYTICS
GOOGLE_ANALYTICS_ID = env('GOOGLE_ANALYTICS_ID', default='')

# hotjar
HOTJAR_ID = None

# SENTRY
SENTRY_DSN = env.str('SENTRY_DSN', default=None)

# Facebook pixel
FACEBOOK_PIXEL_ID = None

# settings-context-processor
TEMPLATE_VISIBLE_SETTINGS = [
    'FACEBOOK_PIXEL_ID',
    'GOOGLE_ANALYTICS_ID',
    'HOTJAR_ID',
    'SENTRY_DSN',
]

# django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, '.webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}


# wagtail related setting
WAGTAIL_SITE_NAME = 'Laboratorium EE'
WAGTAILIMAGES_JPEG_QUALITY = 70


# enable features for wagtail's richtext field
@hooks.register('register_rich_text_features')
def register_extra_features(features):
    features.default_features.extend([
        'blockquote',
        'code',
    ])


RICHTEXT_INLINE_FEATURES = ['bold', 'italic', 'link', 'document-link']
RICHTEXT_BLOCK_FEATURES = [
    'ol', 'ul',
    'image', 'embed',
    'blockquote', 'code',
]


# ### salesforce integration ###

# Environment to use.
#  * production
#    SALESFORCE_DOMAIN = 'login'
#    SALESFORCE_INSTANCE = 'laboratoriumee.my.salesforce.com' (use your SF organization name here)
#
#  * test
#    SALESFORCE_DOMAIN = 'test'
#    SALESFORCE_INSTANCE = 'laboratoriumee--test.my.salesforce.com' (`test` suffix is configurable
#                                                                    via SF sandbox magement page)
#
#  * dummy - suitable for development environments
#    SALESFORCE_DOMAIN = None
#    SALESFORCE_INSTANCE = None
SALESFORCE_DOMAIN = 'login'
SALESFORCE_INSTANCE = 'laboratoriumee.my.salesforce.com'

SALESFORCE_CLIENT_ID = '3MVG9I5UQ_0k_hTmaSws_TCivIpexLZoEP.S63TsK3Sj.3MFQRMclngn44zah.u1dVKpcvH3Bq6d8ejRArxJE'
SALESFORCE_CLIENT_SECRET = env.str('SALESFORCE_CLIENT_SECRET', default=None)
SALESFORCE_REFRESH_TOKEN = env.str('SALESFORCE_REFRESH_TOKEN', default=None)


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
