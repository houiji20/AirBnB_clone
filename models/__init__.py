#!/usr/bin/python3
"""Models to represent everything from users to cities."""

from .engine import FileStorage

storage = FileStorage()
storage.reload()
