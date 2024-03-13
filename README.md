# Concesionaria de Autos "EGO" 🚗🚘🚙
## Introducción:
Proyecto API-REST para EGO basado en una concesionaria de autos.
## Tabla de contenidos:
- [Autor](#autor👀)
- [Tecnologias](#tecnologias-👨‍💻)
- [Entornos Compatibles](#entornos-compatibles-💻)
- [Instalación](#instalación🤖)
- [Modulos](#modulos-🚨)


## Autor👀
- [Pablo Sandoval](https://github.com/SPablo2191)

## Tecnologias 👨‍💻
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)
![Rest Framework](https://img.shields.io/badge/Rest_Framework-3.14.0-brightgreen.svg)

## Entornos Compatibles 💻
![macOS](https://img.shields.io/badge/macOS-compatible-green)
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

## Instalación🤖
Para hacer uso del proyecto de manera local se puede realizar de 2 formas distintas:
### Uso de docker:
1) Basta con disponer [docker engine](https://docs.docker.com/engine/install/) en la computadora ya sea usando [windows](https://docs.docker.com/desktop/install/windows-install/) o [linux](https://docs.docker.com/desktop/install/linux-install/) y ejecutar el siguiente comando:
```cmd
docker-compose up --build
```
2) crear .env en directorio raiz con el siguiente formato:
```json
DB_USER = postgres
DB_PASSWORD = postgres
DB_HOST= db
DB_PORT= 5432
DB_NAME= postgres
```
Se usa un package para leer dicho archivo y cargarlo en el settings.py del proyecto
3) Listo! Ya se puede acceder a la instancia
### Con entorno virtual y base de datos psql
1) Ingresar los siguiente comandos en consola:
```cmd
python3 -m venv [nombreDelEntornoVirtual]
```
este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```cmd
source nombreDelEntornoVirtual/bin/activate
```
NOTA: en caso de trabajar con windows el entorno virtual se genera con scripts para activar el entorno virtual por ende se tiene que acceder de la siguiente forma:
```cmd
nombreDelEntornoVirtual\Scripts\activate.bat
```
y para apagarlo (en ambos casos) es:

```cmd
deactivate
```

2) despues correr el siguiente comando para obtener los paquetes empleados en la API:

```cmd
pip install -r requirements/dev.txt
```
3) crear un archivo .env en el directorio raiz con el siguiente formato:
```json
DB_USER = [Nombre de usuario ej: postgres]
DB_PASSWORD = [Contraseña a poner ej: postgres]
DB_HOST= [host del servicio ej:localhost]
DB_PORT= [puerto que escucha de la bdd ej: 5432]
DB_NAME= [nombre de la db ej:postgres]
```
Se usa un package para leer dicho archivo y cargarlo en el settings.py del proyecto
4) Una vez los paquetes fueron instalados con exito, se debe realizar las migraciones:
```cmd
python manage.py migrate
```
5) Crear un superusuario para acceder al modulo admin:
```cmd
python manage.py createsuperuser
```
6) Levantar el servidor:
```cmd
python manage.py runserver
```
6) ¡Listo! ya puede visitar la pagina web en este [enlace](http://127.0.0.1:8000/).

## Modulos 🚨
- [Vehiculos](#vehiculos)
- [Ficha Tecnica](#ficha-tecnica)
- [Categorías de Vehículos](#categorías-de-vehículos)
- [Características](#características)
- [Secciones](#secciones)
- [Marcas](#marcas)

### Vehiculos

| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | api/vehicles | Registrar un nuevo vehiculo |
| GET   | api/vehicles | Recuperar el listado de vehiculo |
| PATCH    | api/vehicles/<int:id> | Editar un vehiculo por su id |
| DELETE    | api/vehicles/<int:id> | Eliminar un vehiculo de base de datos |

**Ordering:**

Se emplea el siguiente codigo:
```python
ordering_fields = ["model", "year", "price"]
```
para poder filtrar en función de algunos de esos campos:
```bash
GET /api/vehicles/?ordering=year
```
**Filtering:**

Se emplea el siguiente codigo:
```python
filterset_fields = ["vehicle_type", "brand", "year"]
```
para poder filtrar en función de algunos de esos campos:
```bash
GET /api/vehicles/?brand=1
```
**Searching:**

Se emplea el siguiente codigo:
```python
search_fields = ["model"]
```
para poder buscar en función del nombre del vehiculo:
```bash
GET /api/vehicles/?model=hilux
```
retorna:
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "model": "Hilux DX/SR",
            "image_url": "https://maquinac.com/wp-content/uploads/2023/04/Pick-up-Toyota-Hilux-GR-Sport-IV-2.jpg",
            "year": 2020,
            "price": "100000.00",
            "created_at": "2024-03-12T19:17:54.806795Z",
            "updated_at": "2024-03-12T19:17:54.806795Z",
            "vehicle_type": {
                "id": 3,
                "name": "SUVs y Crossovers",
                "description": "Camionetas",
                "created_at": "2024-03-12T19:01:21.208087Z",
                "updated_at": "2024-03-12T19:01:21.208087Z"
            },
            "brand": {
                "id": 1,
                "name": "Toyota",
                "description": "Marca asociada"
            }
        },
        {
            "id": 3,
            "model": "Land Cruiser Prado",
            "image_url": "https://maquinac.com/wp-content/uploads/2023/04/Pick-up-Toyota-Hilux-GR-Sport-IV-2.jpg",
            "year": 2017,
            "price": "815900.00",
            "created_at": "2024-03-12T23:14:41.188191Z",
            "updated_at": "2024-03-12T23:14:41.188191Z",
            "vehicle_type": {
                "id": 3,
                "name": "SUVs y Crossovers",
                "description": "Camionetas",
                "created_at": "2024-03-12T19:01:21.208087Z",
                "updated_at": "2024-03-12T19:01:21.208087Z"
            },
            "brand": {
                "id": 1,
                "name": "Toyota",
                "description": "Marca asociada"
            }
        }
    ]
}
```
### Ficha Tecnica

| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | api/datasheets | Registrar un nuevo data sheet |
| GET   | api/datasheets | Recuperar el listado de data sheet |
| PATCH    | api/datasheets/<int:id> | Editar un data sheet por su id |
| DELETE    | api/datasheets/<int:id> | Eliminar un data sheet de base de datos |

Se emplea el siguiente codigo:
```python
filterset_fields = ["vehicle"]
```
para poder filtrar la data recuperada en función del id de vehiculo:
```bash
GET /api/datasheets/?vehicle=2
```
### Categorías de Vehículos

| Método | Path                     | Descripción                                 |
| ------ | ------------------------ | ------------------------------------------- |
| POST   | api/categories           | Registrar una nueva categoría de vehículo   |
| GET    | api/categories           | Recuperar el listado de categorías de vehículo |
| PATCH  | api/categories/<int:id>  | Editar una categoría de vehículo por su ID  |
| DELETE | api/categories/<int:id>  | Eliminar una categoría de vehículo de la base de datos |

### Características

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| POST   | api/features            | Registrar una nueva característica          |
| GET    | api/features            | Recuperar el listado de características     |
| PATCH  | api/features/<int:id>   | Editar una característica por su ID         |
| DELETE | api/features/<int:id>   | Eliminar una característica de la base de datos |

### Secciones

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| POST   | api/sections            | Registrar una nueva sección                 |
| GET    | api/sections            | Recuperar el listado de secciones           |
| PATCH  | api/sections/<int:id>   | Editar una sección por su ID                |
| DELETE | api/sections/<int:id>   | Eliminar una sección de la base de datos    |

### Marcas

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| POST   | api/brands              | Registrar una nueva marca                   |
| GET    | api/brands              | Recuperar el listado de marcas              |
| PATCH  | api/brands/<int:id>     | Editar una marca por su ID                  |
| DELETE | api/brands/<int:id>     | Eliminar una marca de la base de datos      |



