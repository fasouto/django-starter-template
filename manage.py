#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
    # Add the lib/ directory to the path
    sys.path.append("lib")
    sys.path.append("apps")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
