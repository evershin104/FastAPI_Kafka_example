from settings.config_handler import CONFIG
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"Environment: {dotenv_path}")
load_dotenv(dotenv_path)

print(f"DEVELOP: {os.environ.get('DEVELOP')}")

__all__ = ['CONFIG']