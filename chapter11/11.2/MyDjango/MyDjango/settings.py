

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#+m+r2vq)0fy2r((-=g4(m3betkfhj7ax5hbwf34v^+fb(kb8g'

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
    'index'
]

CACHES = {
    # 默认缓存数据表
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        # TIMEOUT设置缓存的生命周期，以秒为单位，若为None，则永不过期
        'TIMEOUT': 60,
        'OPTIONS': {
            # MAX_ENTRIES代表最大缓存记录的数量
            'MAX_ENTRIES': 1000,
            # 当缓存到达最大数量之后，设置剔除缓存的数量
            'CULL_FREQUENCY': 3,
        }
    },
    # 设置多个缓存数据表
    'MyDjango': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'MyDjango_cache_table',
    }
}

MIDDLEWARE = [
    # 配置全站缓存
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 使用中文
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 配置全站缓存
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]
# # 设置缓存的生命周期
# CACHE_MIDDLEWARE_SECONDS = 15
# # 设置缓存数据保存在数据表my_cache_table中
# # 属性值default来自于缓存配置CACHES的default属性
# CACHE_MIDDLEWARE_ALIAS = 'default'
# # 设置缓存表字段cache_key的值
# # 用于同一个Django项目多个站点之间的共享缓存
# CACHE_MIDDLEWARE_KEY_PREFIX = 'MyDjango'


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
