#from django.apps import AppConfig
from __core__.infra.common.app_config import AppConfig

class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
