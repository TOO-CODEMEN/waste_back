import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()

class MlSettings(BaseSettings):
    api_key: SecretStr = os.getenv("Robo_API")