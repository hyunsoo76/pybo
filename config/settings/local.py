from .base import *
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_HOSTS = ['*']

# --- vendor autocomplete API allow hosts ---
ALLOWED_HOSTS = list(set((globals().get("ALLOWED_HOSTS") or []) + [
    "3.37.211.248",
    "127.0.0.1",
    "localhost",
]))