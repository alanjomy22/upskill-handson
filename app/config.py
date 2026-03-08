from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    APP_ENV: str = "development"   # default value
    PORT: int = 8000               # auto-converts "8000" string → int

    class Config:
        env_file = ".env"          # tells Pydantic where to look

settings = Settings()              # reads & validates on import
