#!/usr/bin/env python
"""Command-line entry point for the RUHAMAH website."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ruhamah.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
