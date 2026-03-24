import os
from django.core.wsgi import get_wsgi_application

# แก้เป็น 'settings' เฉยๆ เพราะไฟล์ settings.py อยู่ข้างๆ wsgi.py เลย
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()