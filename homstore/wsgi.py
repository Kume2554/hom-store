import os
from django.core.wsgi import get_wsgi_application

# ใช้จุดเชื่อมชื่อโฟลเดอร์กับ settings ห้ามใช้ / และห้ามมี .py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homstore.settings')

application = get_wsgi_application()