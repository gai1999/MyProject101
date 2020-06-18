"""
Django settings for typeidea project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6)uwfo+1*u@3h4c5168&!$=_yq90dvi-#mrav*i&59%9d)ni7e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'ckeditor',  #可视化编辑器 pip install django-ckeditor
    'ckeditor_uploader',
    'typeidea',  # 因为templates模板被定义在这个总目录下, 所以需要注册这个目录app
    'blog',
    'comment',
    'config',
     # pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
    'xadmin',
    'crispy_forms',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # 访问限制
    'blog.middleware.access_restrictions.AccessRestrictionsMiddleware',
    # pv uv 访问统计中间件
    'blog.middleware.user_id.UserIDMiddleware',
    # 限制用户非法提交大量垃圾评论
    'blog.middleware.comment_filter.CommentFilterMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'typeidea.urls'

#THEME = 'bootstrap'  # 多种前端样式自由变换 修改次变量即可
THEME = 'coolblog'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'typeidea.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": os.getenv('MY_REDIS_PW')
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 邮件通知
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25 # 大多都是25；若使用SSL，端口号465或587
EMAIL_HOST_USER = "gai520website@163.com" #发送邮箱
EMAIL_HOST_PASSWORD = os.getenv('MY_SMTP_PW') # 使用的是QQ的授权码，不是你的密码
EMAILE_USE_TLS = True #一定要是True，否则发不了
EMAIL_FROM = "gai520website@163.com" #邮件发送人(邮件中所显示的发送人，和EMAIL_HOST_USER同)
EMAIL_TO = ['643177348@qq.com','17610139558@163.com']

# 绑定的域名
HOST_NAME = 'http://192.168.0.108:8000'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/tmp/static'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'themes', THEME, 'static'),]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# xadmin管理后台
XADMIN_TITLE = '满满屋-记录你的生活每一天'
XADMIN_FOOTER_TITLE = 'Power By gai520.com'

# 配置 ckeditor富文本编辑器
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': 800,
        'tabSpaces': 4,
        'extraPlugins': 'codesnippet,uploadimage',  # 配置代码插件, uploadimage 拖动上传
    }
}

CKEDITOR_UPLOAD_PATH = 'article_images'  # 文件上传路径
CKEDITOR_RESTRICT_BY_USER = True  # 限制用户在编辑器中只能查看自己上传的文件
# CKEDITOR_IMAGE_BACKEND = True  # 使用图片缩略图
# CKEDITOR_ALLOW_NONIMAGE_FILES = False  # 只允许上传图片

# 图片水印名称
IMAGE_WATERMARK_TEXT = '@gai520.com'
DEFAULT_FILE_STORAGE = 'typeidea.storage.WatermarkStorage'