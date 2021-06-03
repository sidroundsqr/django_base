"""This file is local env. settings file to run django"""

from .base import * # pylint: disable=wildcard-import, unused-wildcard-import

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

#- SERVER TYPE
SERVER_TYPE = 'local'
