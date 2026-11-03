import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "replace-this-with-an-environment-secret-before-deployment")
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "testserver",
    ".vercel.app",
    "ruhamah-wear.vercel.app",
]

env_allowed_hosts = os.getenv("ALLOWED_HOSTS")
if env_allowed_hosts:
    ALLOWED_HOSTS.extend([host.strip() for host in env_allowed_hosts.split(",") if host.strip()])

CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
    "https://ruhamah-wear.vercel.app",
]

env_csrf_origins = os.getenv("CSRF_TRUSTED_ORIGINS")
if env_csrf_origins:
    CSRF_TRUSTED_ORIGINS.extend([origin.strip() for origin in env_csrf_origins.split(",") if origin.strip()])

INSTALLED_APPS = ["django.contrib.staticfiles", "atelier"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "ruhamah.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
}]
WSGI_APPLICATION = "ruhamah.wsgi.application"
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/Warsaw"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
