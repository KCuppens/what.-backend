from .base import *  # noqa: F401, F403, pylint: disable=wildcard-import, unused-wildcard-import
from .base import env


# GENERAL
# ------------------------------------------------------------------------------

# Be sure to still throw if not defined as before
env("SECRET_KEY")
