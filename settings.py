import os

from ecommerce.ecommerce.settings import BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # تأكد أن المسار صحيح


ALLOWED_HOSTS = [
    'web-production-e9b9.up.railway.app',  # أضف نطاق Railway
    'localhost',  # للسماح بالتشغيل المحلي
    '127.0.0.1',  # التشغيل على الجهاز المحلي
]
