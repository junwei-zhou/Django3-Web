

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@p_m^!ha=$6m$9#m%gobzo&b0^g2obt4teod84xs6=f%$4a66x'

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
    'user',
    # 添加第三方应用
    'social_django'
]

# 设置第三方的OAuth2.0
AUTHENTICATION_BACKENDS = (
    # 微博的功能
    'social.backends.weibo.WeiboOAuth2',
    # QQ的功能
    'social.backends.qq.QQOAuth2',
    # 微信的功能
    'social.backends.weixin.WeixinOAuth2',
    'django.contrib.auth.backends.ModelBackend',)
# 注册成功后跳转页面
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'user:success'
# 开放平台应用的 APPID 和 SECRET
SOCIAL_AUTH_WEIBO_KEY = '692671009'
SOCIAL_AUTH_WEIBO_SECRET = 'd2c4440e1a6d7950b1585cc58334a527'
SOCIAL_AUTH_QQ_KEY = 'APPID'
SOCIAL_AUTH_QQ_SECRET = 'SECRET'
SOCIAL_AUTH_WEIXIN_KEY = 'APPID'
SOCIAL_AUTH_WEIXIN_SECRET = 'SECRET'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyDjango.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
