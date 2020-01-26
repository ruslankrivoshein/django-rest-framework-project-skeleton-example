from .db import DATABASES
from .django import *
from .rest import REST_FRAMEWORK


try:
    from .settings_local import *
except ImportError:
    pass
