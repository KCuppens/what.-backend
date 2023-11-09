# Production settings. To be used for every production deployment (staging, dev, prod).
import logging

from .base import *  # noqa: F401, F403, pylint: disable=wildcard-import, unused-wildcard-import
from .base import env


# GENERAL
# ------------------------------------------------------------------------------

# Be sure to still throw if not defined as before
env("DJANGO_SECRET_KEY")