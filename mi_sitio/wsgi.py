"""
WSGI config for mi_sitio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi_sitio.settings")

if os.environ.get("VERCEL") == "1" and not os.environ.get("DB_HOST"):
    import django

    django.setup()
    from django.core.management import call_command

    call_command("migrate", "--noinput")

application = get_wsgi_application()
