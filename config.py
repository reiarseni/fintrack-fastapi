from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "cambia_esta_clave_secreta_en_produccion"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./finance.db"

settings = Settings()
