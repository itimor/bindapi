# -*- coding: utf-8 -*-
# author: kiven

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bindapi.settings")

application = get_wsgi_application()
