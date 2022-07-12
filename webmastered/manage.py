#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    docker = os.environ.get('DOCKER', False)
    if docker:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webmastered.settings.docker")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webmastered.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
