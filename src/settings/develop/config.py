from settings.base_config import BaseConfig
import environ


env = environ.Env()


class DevelopConfig(BaseConfig):
    """Default develop env. config for FastAPI
    
    Note:
        If You want to add env. variables - make sure You added them in BaseConfig with default value 
        and added into DevelopConfig and ProductionConfig.
    """
    PLATFORM: str = 'Конфигурация разработчиков'
    
    APP_PORT: int = env('APP_PORT', default=8000, parse_default=int)

    DEVELOP: bool = env('DEVELOP', default=True, parse_default=bool)
    DEBUG: bool = env('DEBUG', default=True, parse_default=bool)      # TODO logging

    KAFKA_BOOTSTRAP_SERVERS: str = env('KAFKA_BOOTSTRAP_SERVERS', default='kafka:9092',
                                       parse_default=str)
    TOPIC: str = env('TOPIC', default='registration', parse_default=str)
    CONSUME_TOPIC: str = env('TOPIC', default='registration', parse_default=str)

    DATABASE_URL: str = env('DATABASE_URL', default='', parse_default=str)

    REDIS_HOST: str = env('REDIS_HOST', default='redis', parse_default=str)
    REDIS_PORT: int = env('REDIS_PORT', default=6379, parse_default=int)
