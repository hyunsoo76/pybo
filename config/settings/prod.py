from .base import *

ALLOWED_HOSTS = ['3.37.211.248']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = True

# --- Allow hosts for vendor autocomplete API / health checks ---
ALLOWED_HOSTS = list(set((globals().get("ALLOWED_HOSTS") or []) + [
    "3.37.211.248",
    "127.0.0.1",
    "localhost",
]))