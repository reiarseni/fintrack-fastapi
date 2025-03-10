# Sistema de Finanzas Personales con FastAPI

## Estructura del Proyecto

```
finanzas_app/
│
├── main.py                 # Punto de entrada de la aplicación
├── database.py             # Configuración de la base de datos
├── models.py               # Modelos SQLAlchemy
├── schemas.py              # Esquemas Pydantic
├── crud.py                 # Operaciones CRUD
├── auth.py                 # Lógica de autenticación
├── dependencies.py         # Dependencias de FastAPI
├── config.py               # Configuración de la aplicación
│
├── routers/
│   ├── __init__.py
│   ├── auth.py             # Rutas de autenticación (login, registro)
│   ├── transactions.py     # Rutas para gestionar transacciones
│   └── categories.py       # Rutas para gestionar categorías
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
├── templates/
│   ├── base.html           # Plantilla base
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── transactions/
│   │   ├── list.html
│   │   └── form.html
│   └── categories/
│       ├── list.html
│       └── form.html
│
├── requirements.txt        # Dependencias del proyecto
└── .gitignore              # Archivo .gitignore
```

## Instrucciones de Instalación

Sigue estos pasos para configurar y ejecutar el proyecto:

1. Crea un entorno virtual:
```bash
python -m venv venv
```

2. Activa el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```bash
uvicorn main:app --reload
```

5. Abre un navegador y visita: http://127.0.0.1:8000

## Explicación de la Estructura

- **main.py**: Punto de entrada que configura FastAPI y los routers
- **database.py**: Configuración de SQLAlchemy y SQLite
- **models.py**: Definición de modelos de datos (Usuario, Categoría, Transacción)
- **schemas.py**: Esquemas Pydantic para validación de datos
- **crud.py**: Funciones para operaciones CRUD
- **auth.py**: Gestión de autenticación con JWT en cookies
- **dependencies.py**: Dependencias de FastAPI para inyección
- **routers/**: Módulos con rutas organizadas por funcionalidad
- **templates/**: Plantillas HTML con Jinja2
- **static/**: Archivos estáticos (CSS, JS, imágenes)

## Funcionalidades

1. **Sistema de autenticación**:
   - Registro de usuarios
   - Inicio de sesión con JWT almacenado en cookies
   - Cierre de sesión

2. **Gestión de categorías**:
   - Crear, listar, editar y eliminar categorías
   - Categorías separadas por tipo (ingreso/gasto)

3. **Gestión de transacciones**:
   - Crear, listar, editar y eliminar transacciones
   - Filtrado automático de categorías según el tipo de transacción
   - Visualización clara con códigos de color

## Notas Adicionales

- La aplicación sigue el principio KISS, manteniendo la estructura simple pero funcional
- Se implementa protección de rutas mediante dependencias de FastAPI
- El sistema de cookies asegura que solo usuarios autenticados accedan a las funcionalidades
- Bootstrap 5 se utiliza para el diseño responsive sin necesidad de CSS personalizado
- Se incluye un .gitignore que excluye la base de datos SQLite y otros archivos no necesarios
