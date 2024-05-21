from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Disable debug mode
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True  # If it is true all the allowed origins can access. And it restricts CORS_ALLOWED_ORIGINS settings.

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Language',
    'Content-Type',
    'Authorization',
    'organization',
    'token'
]

#
# # Set your production domain(s) here
# ALLOWED_HOSTS = ['your-domain.com']
#
# # Database configuration
#
# # Static files configuration
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
#
# # Media files configuration
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
#
# # Security settings
# SECRET_KEY = 'your-secret-key'
#
# # Additional security settings (optional)
# # ...
#
# # Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'your-smtp-host'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'your-email@example.com'
#
# # Logging configuration
# # Configure logging handlers, loggers, and formatters here
#
# # Other production-specific settings
# # ...
