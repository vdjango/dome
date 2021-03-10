import sys
# from .celery import app

sys_path = [
    '/usr/lib/python3.6/site-packages',
    '/usr/lib64/python3.6/site-packages',
    '/usr/local/lib/python3.6/site-packages',
]

for i in sys_path:
    sys.path.append(i)

