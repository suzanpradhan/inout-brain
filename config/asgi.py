"""
ASGI config for brain project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

import environ
from django.core.asgi import get_asgi_application

env = environ.Env()
environ.Env.read_env(env_file=".env")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    env.str("DJANGO_SETTINGS_MODULE", default="config.settings.production"),
)

application = get_asgi_application()
