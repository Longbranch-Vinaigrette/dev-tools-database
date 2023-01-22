#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from src.submodules.dev_tools_utils import tests


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DatabaseServer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Tests
    routes_path = f"{os.getcwd()}{os.path.sep}src{os.path.sep}routes"
    tests.test_dynamic_imports_routes(routes_path)

    # Main stuff
    main()
