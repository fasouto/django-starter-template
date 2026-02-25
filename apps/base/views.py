import sys

import django
from django.conf import settings
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    db_ok = False
    db_is_postgres = False
    try:
        connection.ensure_connection()
        db_ok = True
        db_is_postgres = connection.vendor == "postgresql"
    except Exception:
        pass

    secret_key = settings.SECRET_KEY
    secret_changed = secret_key not in ("django-insecure-dev-key-change-me", "build-time-placeholder", "change-me-to-a-random-string")
    rv = '<a href="https://docs.railway.com/variables" target="_blank">Railway variables</a>'
    checklist = [
        ("Database connected", "Set DATABASE_URL in .env or {}".format(rv), db_ok),
        ("PostgreSQL configured", "Use postgres:// instead of sqlite:///", db_is_postgres),
        ("SECRET_KEY changed", "Set a unique key in .env or {}".format(rv), secret_changed),
        ("DEBUG is off", "Set DEBUG=False in production", not settings.DEBUG),
        ("Set ALLOWED_HOSTS", "Add your domain to ALLOWED_HOSTS in {}".format(rv), not settings.DEBUG and len(settings.ALLOWED_HOSTS) > 0),
        ("Configure CSRF_TRUSTED_ORIGINS", "Add https://yourdomain to CSRF_TRUSTED_ORIGINS in {}".format(rv), len(settings.CSRF_TRUSTED_ORIGINS) > 0 if hasattr(settings, "CSRF_TRUSTED_ORIGINS") else False),
        ("Edit this page", "apps/base/templates/base/home.html", False),
    ]

    return render(
        request,
        "base/home.html",
        {
            "django_version": django.get_version(),
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "db_status": db_ok,
            "checklist": checklist,
        },
    )


def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "ok", "database": "ok"})
    except Exception as e:
        return JsonResponse({"status": "error", "database": str(e)}, status=500)
