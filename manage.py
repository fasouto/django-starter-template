#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Read .env file before setting defaults so local DJANGO_SETTINGS_MODULE is respected
    try:
        import environ

        environ.Env.read_env(os.path.join(os.path.dirname(__file__), ".env"))
    except (ImportError, FileNotFoundError):
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
