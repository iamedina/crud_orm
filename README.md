# API de Inventario (ORM)

API REST desarrollada con **Flask** y **SQLAlchemy** para gestionar productos, categorías y entradas de inventario. Incluye documentación interactiva con **Swagger** (Flasgger) y una colección de **Postman** para probar los endpoints.

## Tecnologías

- Python 3
- Flask 3
- Flask-SQLAlchemy (ORM)
- MySQL + PyMySQL
- Flasgger (Swagger UI)
- Flask-CORS
- Postman (colección de pruebas)

## Estructura del proyecto

```
ORM/
├── backend/
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── requeriments.txt        # Dependencias del proyecto
│   └── app/
│       ├── common/             # Configuración y manejo de errores
│       ├── controller/         # Blueprints y rutas (endpoints)
│       ├── models/             # Modelos ORM (Producto, Categoria, Entrada)
│       └── services/           # Lógica de negocio y acceso a datos
├── frontend/                   # (pendiente)
└── postman/                    # Recursos de Postman
```

## Requisitos previos

- Python 3.10 o superior
- MySQL en ejecución
- Base de datos creada:

```sql
CREATE DATABASE db_products CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Instalación

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requeriments.txt
```

En Linux/macOS la activación del entorno es:

```bash
source venv/bin/activate
```

## Configuración de la base de datos

Los datos de conexión están en `backend/app/common/config.py`:

```python
USER = "root"
PASSWORD = "root"
HOST = "localhost"
DATABASE = "db_products"
```

Ajusta esos valores según tu instalación local de MySQL. Las tablas se crean automáticamente al iniciar la aplicación (`db.create_all()`).

## Ejecución

Desde la carpeta `backend`:

```powershell
python main.py
```

La API queda disponible en:

- API: <http://localhost:5000>
- Documentación Swagger: <http://localhost:5000/apidocs>

## Endpoints

### Generales

| Método | Ruta | Descripción |
| ------ | ---- | ----------- |
| GET | `/` | Verifica que la API esté funcionando |

### Productos

| Método | Ruta | Descripción |
| ------ | ---- | ----------- |
| GET | `/products` | Lista todos los productos |
| GET | `/products/<id>` | Consulta un producto por ID |
| POST | `/products` | Crea un producto |
| PUT | `/products/<id>` | Actualiza un producto |
| DELETE | `/products/<id>` | Elimina un producto |

Ejemplo de creación:

```json
{
  "nombre": "Manzana",
  "descripcion": "Manzana Chilena",
  "precio": 10.5,
  "categoria_id": 1,
  "stock_min": 5,
  "disponible": true
}
```

### Categorías

| Método | Ruta | Descripción |
| ------ | ---- | ----------- |
| GET | `/categorias` | Lista todas las categorías |
| GET | `/categorias/<id>` | Consulta una categoría por ID |
| POST | `/categorias` | Crea una categoría |
| PUT | `/categorias/<id>` | Actualiza una categoría |
| DELETE | `/categorias/<id>` | Elimina una categoría |

Ejemplo de creación:

```json
{
  "nombre": "Electrónica",
  "descripcion": "Productos electrónicos"
}
```

### Entradas

| Método | Ruta | Descripción |
| ------ | ---- | ----------- |
| GET | `/entradas` | Lista todas las entradas |
| GET | `/entradas/<id>` | Consulta una entrada por ID |
| POST | `/entradas` | Registra una entrada |
| PUT | `/entradas/<id>` | Actualiza una entrada |
| DELETE | `/entradas/<id>` | Elimina una entrada |

Ejemplo de creación:

```json
{
  "entra_producto_id": 1,
  "entra_cantidad": 10,
  "entra_factura": "FAC-001",
  "entra_stand": "A1",
  "entra_ubicacion": "Bodega Central"
}
```

## Códigos de respuesta

| Código | Significado |
| ------ | ----------- |
| 200 | Operación exitosa |
| 201 | Recurso creado |
| 400 | Solicitud incorrecta o datos faltantes |
| 404 | Recurso no encontrado |
| 409 | Conflicto (por ejemplo, eliminar un producto con entradas asociadas) |
| 422 | Validación fallida |
| 500 | Error interno del servidor |

## Colección de Postman

La carpeta `postman/` contiene los recursos del workspace (colecciones, entornos, mocks y specs). Puedes abrirlos directamente desde Postman o ejecutarlos con la CLI de Postman.

## Autor

Proyecto desarrollado como parte de la formación del **SENA**.
