from settings.develop.config import DevelopConfig
from settings.production.config import ProductionConfig
import os


if os.environ.get('DEVELOP'):
    """Handle the right one pydantic-settings class by 
    environment variable"""
    CONFIG = ProductionConfig()
else:
    CONFIG = DevelopConfig()
