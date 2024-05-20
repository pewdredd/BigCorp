from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-fab)g_p5%z4ek_p2__gf87)^z24u*%8d(4dqd-hvof+@r5u3+*'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop.apps.ShopConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'owndjangoproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'shop.context_processors.categories'
            ],
        },
    },
]

WSGI_APPLICATION = 'owndjangoproj.wsgi.application'


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


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


INSTRUCTION = 'зарегать новую апку - cart, сделай: urls, views(cart_view/add/delete/update). Сделай корзину на основе request.session сам знаешь для чего. Сделай контекст процессор для юза корзины. cart-view.html,  + render - cart_view. Корзина - это ключ сессии, ну так подумай и сделай это. Доделай cart_add, проверяя if POST.action == post то бери из requesta все данные о продукте, создай этот продукт, и добавь его в корзину, методом add который тебе нужно реализовать в корзине в конце поставив modified = True. Доработай cart_view добавив туда корзину для шаблона. Потом в шаблоне нужно показать продукты в корзине через цикл, ну так вот тебе надо корзину итератором сделать, сначала создай копию корзины потом отфильтруй продуктыпрокси через id в ключах корзины, и в копию корзины добавь продукты отфильтрованные по id а потом через yield возвращай необходимые данные из каждого значения корзины копии. Потом добавь метод get_total_price. Дальше добавь сделай вьюху по удалению, через метод delete корзины, ну и добавь этот метод - удаления продукта из корзины. И также добавь метод update в корзину. А потом после удаления надо обновить данные total_price  через JsonResponce. Ну и добавь cart_update во вьюхи. Ну и тесты скопируй. А потом сделай коммит.'
INSTRUCTION2 = 'Зарегай новую аппку - account. django-crispy-forms, django-email-verification. Создай UserCreateForm, в Meta пропиши модель и fields. В init - super'
