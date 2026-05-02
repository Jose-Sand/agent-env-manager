import os
from dotenv import load_dotenv

class Config:
    def __init__(self, env_name: str):
        self.env_name = env_name
        self.variables = {}
        self.database_config = {}

    @classmethod
    def load(cls, env_name: str):
        config = cls(env_name)
        load_dotenv(f".{env_name}.env")
        config.variables = {key: os.getenv(key) for key in os.environ.keys()}
        return config

    @property
    def db_config(self):
        if not self.database_config:
            database_url = os.getenv("DATABASE_URL")
            if database_url:
                import psycopg2
                from psycopg2.extras import parse_dsn
                parsed_db_config = parse_dsn(database_url)
                self.database_config = {
                    "username": parsed_db_config["user"],
                    "password": parsed_db_config["password"],
                    "host": parsed_db_config["host"],
                    "port": parsed_db_config["port"],
                    "database": parsed_db_config["dbname"]
                }
        return self.database_config

    def get_variable(self, variable_name: str):
        return os.getenv(variable_name)

    @classmethod
    def create_env_file(cls, env_name: str):
        with open(f".{env_name}.env", "w") as f:
            pass