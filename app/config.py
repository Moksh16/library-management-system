from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_port : str
    database_username : str 
    secret_key : str
    database_hostname: str
    database_password:str
    database_name: str
    algorithm: str
    access_token_expire_minutes: int
    database_sslmode: str
 
    class Config:
        env_file = ".env"
    

settings = Settings()