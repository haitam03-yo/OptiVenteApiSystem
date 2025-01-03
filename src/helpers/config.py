from fastapi import FastAPI, Depends
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    APP_NAME: str
    APP_VERSION: str
    


def get_settings() -> Settings:
    return Settings()