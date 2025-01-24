from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    IMEI_SANDBOX_TOKEN: str
    DATABASE: str
    BOT_TOKEN: str
    
    class Config:
        env_file = '.env'
        
settings = Settings()