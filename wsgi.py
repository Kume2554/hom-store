import os
from django.core.wsgi import get_wsgi_application

# ต้องระบุชื่อโฟลเดอร์ที่เก็บ settings.py ให้ถูก
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homstore.settings')

application = get_wsgi_application()