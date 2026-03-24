import os
from django.core.wsgi import get_wsgi_application

# ตรงนี้ต้องเป็น 'homstore.settings' (ใช้จุด . เท่านั้น ห้ามใช้ /)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homstore.settings')

application = get_wsgi_application()