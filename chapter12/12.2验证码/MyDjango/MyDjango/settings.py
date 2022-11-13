

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
    # 添加验证码功能
    'captcha'
]

# Django Simple Captcha的基本配置
# 设置验证码的显示顺序
# 一个验证码识别包含文本输入框、隐藏域和验证码图片
# CAPTCHA_OUTPUT_FORMAT是设置三者的显示顺序
CAPTCHA_OUTPUT_FORMAT = '%(text_field)s %(hidden_field)s %(image)s'
# 设置图片噪点
CAPTCHA_NOISE_FUNCTIONS = ( # 设置样式
                            'captcha.helpers.noise_null',
                            # 设置干扰线
                           'captcha.helpers.noise_arcs',
                            # 设置干扰点
                           'captcha.helpers.noise_dots',
                           )
# 图片大小
CAPTCHA_IMAGE_SIZE = (100, 25)
# 设置图片背景颜色
CAPTCHA_BACKGROUND_COLOR = '#ffffff'
# 图片中的文字为随机英文字母
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为英文单词
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
# 图片中的文字为数字表达式
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# 设置字符个数
CAPTCHA_LENGTH = 4
# 设置超时(minutes)
CAPTCHA_TIMEOUT = 1

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


# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'public_static'),]
STATIC_URL = '/static/'
