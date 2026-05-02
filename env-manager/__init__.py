import os
import dotenv
from typing import Dict, List

class EnvironmentManager:
    def __init__(self):
        self.envs = {}

    def load_dotenv(self, filename: str) -> None:
        """Carga las variables de entorno desde un archivo .env"""
        dotenv.load_dotenv(filename)

    def create_env(self, name: str, vars: Dict[str, str] = {}) -> None:
        """Crear un nuevo entorno con la configuración dada"""
        self.envs[name] = vars

    def get_env(self, name: str) -> Dict[str, str]:
        """Obtiene el entorno con el nombre dado"""
        return self.envs.get(name)

    def set_env(self, name: str, vars: Dict[str, str]) -> None:
        """Establece las variables de entorno para un entorno existente"""
        if name in self.envs:
            self.envs[name].update(vars)
        else:
            raise ValueError(f"Entorno '{name}' no existe")

    def delete_env(self, name: str) -> None:
        """Elimina el entorno con el nombre dado"""
        if name in self.envs:
            del self.envs[name]
        else:
            raise ValueError(f"Entorno '{name}' no existe")


def get_env_vars() -> Dict[str, str]:
    """Obtiene las variables de entorno actuales"""
    return {key: value for key, value in os.environ.items() if not key.startswith('ENV_')}


class DatabaseConfig:
    def __init__(self):
        self.configs = {}

    def add_config(self, name: str, host: str, db: str, user: str, password: str) -> None:
        """Agregar una configuración de base de datos"""
        self.configs[name] = {
            'host': host,
            'database': db,
            'user': user,
            'password': password
        }

    def get_config(self, name: str) -> Dict[str, str]:
        """Obtiene la configuración de base de datos con el nombre dado"""
        return self.configs.get(name)


# Inicializa los manejadores de entornos y bases de datos
env_manager = EnvironmentManager()
db_config = DatabaseConfig()

def main():
    # Carga las variables de entorno desde un archivo .env
    env_manager.load_dotenv('.env')

    # Crear un nuevo entorno con la configuración dada
    env_manager.create_env('dev', {
        'VARIABLE1': 'valor1',
        'VARIABLE2': 'valor2'
    })

    # Obtiene el entorno con el nombre dado
    dev_env = env_manager.get_env('dev')

    # Establece las variables de entorno para un entorno existente
    env_manager.set_env('dev', {
        'VARIABLE3': 'valor3',
        'VARIABLE4': 'valor4'
    })

    # Obtiene la configuración de base de datos con el nombre dado
    db_config.add_config('default', 'localhost', 'mi_base_de_datos', 'usuario', 'contraseña')
    default_db = db_config.get_config('default')

if __name__ == '__main__':
    main()