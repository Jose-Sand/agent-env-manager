# Gestor de entornos de desarrollo - env-manager
=====================================================

Un gestor de entornos de desarrollo que permite crear y administrar fácilmente diferentes configuraciones de entorno para proyectos.

## Características
-----------------

*   Creación y administración de entornos
*   Definición de variables de entorno
*   Configuraciones de base de datos

## Badges
--------

[![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-orange.svg)](https://www.python.org/)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Instalación
------------

```bash
pip install -r requirements.txt
```

O bien, si deseas instalarlo globalmente:

```bash
pip install env-manager
```

## Uso
-----

### Crear un entorno

Puedes crear un nuevo entorno ejecutando el comando `env-manager create` y siguiendo las instrucciones.

### Configurar variables de entorno

Puedes definir variables de entorno en el archivo `config.py`. Por ejemplo:

```python
# env-manager/config.py
DATABASE_URL = 'postgresql://user:password@localhost/dbname'
```

Luego, puedes utilizar estas variables con `env-manager`.

### Configuración de base de datos

Puedes configurar la conexión a una base de datos ejecutando el comando `env-manager db configure` y siguiendo las instrucciones.

## Estructura del proyecto
-------------------------

```markdown
env-manager/
|---- env_manager/
|       |---- __init__.py
|       |---- main.py
|       |---- config.py
|---- tests/
|       |---- test_env_manager.py
|---- requirements.txt
|---- package.json
```

## Contribución
-------------

Si deseas contribuir al proyecto, por favor lee el [Código de conducta](https://github.com/usuario/env-manager/blob/master/CODE_OF_CONDUCT.md) y haz una solicitud de cambio en GitHub.

## Licencia
-----------

env-manager se distribuye bajo la licencia MIT. Por favor consulta el archivo `LICENSE` para obtener más información sobre los términos de uso.