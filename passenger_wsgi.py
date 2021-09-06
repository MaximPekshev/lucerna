# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1457472/data/www/shar31.com/lucerna')
sys.path.insert(1, '/var/www/u1457472/data/sharenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lucerna.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()