from .base import *
from google.oauth2 import service_account

DEBUG = False

# static files config
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# media files config
MEDIA_URL = os.environ.get('GS_BUCKET_URL')
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = os.environ.get('GS_BUCKET_NAME')
GS_LOCATION = os.environ.get('GS_LOCATION')
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "/tmp/gcloud-service-key.json"
)
