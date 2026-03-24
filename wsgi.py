import os
from django.core.wsgi import get_wsgi_application

# ระบุชื่อโฟลเดอร์หลัก . ชื่อไฟล์ settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homstore.settings')

application = get_wsgi_application()