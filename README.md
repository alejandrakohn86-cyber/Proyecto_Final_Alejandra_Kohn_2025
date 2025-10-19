# 📝 ProyectoFinalHidalgo - Sistema de Gestión con Python y Django

Aplicación web que simula un sistema de gestión empresarial desarrollada en Python con Django, que incluye gestión de páginas, productos, clientes, sistema de autenticación completo y mensajería entre usuarios.

## 📋 Descripción

Este proyecto es una aplicación web multifuncional que combina las características de un blog con un sistema de gestión empresarial. Permite a los usuarios autenticados crear y gestionar páginas de contenido, productos, clientes individuales y corporativos, además de comunicarse entre sí mediante un sistema de mensajería interno.

## ✨ Características Principales

### 🔐 Sistema de Autenticación
- Registro de usuarios con username, email y password
- Login y logout
- Perfiles de usuario personalizables con:
  - Avatar/foto de perfil
  - Información personal (nombre, apellido, email)
  - Biografía personalizada
  - Cambio de contraseña
  - Edición de perfil

### 📄 Gestión de Páginas (Blog)
- **CRUD completo** para páginas/posts:
  - Crear páginas con editor de texto enriquecido (CKEditor)
  - Listar todas las páginas
  - Ver detalle de cada página
  - Editar páginas existentes
  - Eliminar páginas
- Campos incluyen: título, subtítulo, contenido enriquecido, imagen y fechas
- Solo usuarios autenticados pueden crear, editar o eliminar páginas
- Todos pueden ver las páginas publicadas

### 📦 Gestión de Productos
- **CRUD completo** para productos
- Características por producto:
  - Código SKU único
  - Nombre y descripción
  - Precio y stock
  - Categorías (Electrónica, Indumentaria, Alimentos, Hogar)
  - Imagen del producto
- Búsqueda de productos por múltiples criterios
- Indicadores visuales de stock (Agotado, Stock bajo, Disponible)
- Vistas protegidas: solo usuarios autenticados pueden modificar

### 👥 Gestión de Clientes
- **Clientes Individuales:**
  - Datos personales completos
  - Documento, teléfono, domicilio
  - Tipo de cliente
  - Historial de registro
- **Clientes Corporativos:**
  - Razón social y nombre de fantasía
  - CUIT
  - Representante legal vinculado
  - Información de contacto
- **CRUD completo para ambos tipos**
- Permisos: solo usuarios autenticados pueden gestionar clientes

### 💬 Sistema de Mensajería
- Mensajería interna entre usuarios registrados
- Funcionalidades:
  - Bandeja de entrada
  - Mensajes enviados
  - Redactar nuevos mensajes
  - Responder mensajes
  - Eliminar mensajes
  - Indicador de mensajes no leídos
  - Marcado automático como leído al visualizar

### 🎨 Interfaz de Usuario
- Diseño moderno y responsive
- Navegación intuitiva con navbar
- Cards visuales para productos, clientes y páginas
- Mensajes de éxito/error
- Botones de acción contextuales

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.12 con Django 5.0.0
- **Base de datos:** SQLite3 (desarrollo)
- **Editor de texto:** CKEditor 6.7.0
- **Procesamiento de imágenes:** Pillow 10.1.0
- **Frontend:** HTML5, CSS3, JavaScript
- **Control de versiones:** Git

## 📁 Estructura del Proyecto

```
ProyectoFinalHidalgo/
├── accounts/              # App de autenticación y perfiles
├── clientes_app/          # App principal (productos, clientes)
├── messenger/             # App de mensajería
├── pages/                 # App de blog/páginas
├── templates/             # Templates HTML
│   ├── accounts/
│   ├── clientes_app/
│   ├── messenger/
│   ├── pages/
│   └── base.html
├── static/                # Archivos estáticos CSS/JS
├── media/                 # Archivos subidos por usuarios
├── manage.py
├── requirements.txt
└── README.md
```

## 📦 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/sebasshidalgo/ProyectoFinalHidalgo.git
cd ProyectoFinalHidalgo
```

### 2. Crear y activar entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (opcional pero recomendado)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear un usuario administrador.

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 🎯 Uso de la Aplicación

### Acceso Inicial
1. Abre tu navegador y ve a `http://127.0.0.1:8000/`
2. Regístrate como nuevo usuario o inicia sesión
3. Explora las diferentes secciones desde el menú de navegación

### Panel de Administración
- Accede a: `http://127.0.0.1:8000/admin/`
- Usa las credenciales del superusuario creado anteriormente
- Desde aquí puedes gestionar todos los modelos

### Funcionalidades por Sección

**📄 Pages (Blog):**
- `/pages/` - Ver todas las páginas
- `/pages/create/` - Crear nueva página (requiere login)
- `/pages/<id>/` - Ver detalle de una página
- `/pages/<id>/edit/` - Editar página (requiere login)

**📦 Productos:**
- `/productos/` - Catálogo de productos
- `/productos/nuevo/` - Agregar producto (requiere login)
- `/buscar/` - Buscar productos

**👥 Clientes:**
- `/clientes/` - Lista de clientes
- `/clientes-corporativos/` - Clientes corporativos

**💬 Mensajes:**
- `/messages/inbox/` - Bandeja de entrada
- `/messages/sent/` - Mensajes enviados
- `/messages/compose/` - Nuevo mensaje

**👤 Perfil:**
- `/accounts/perfil/` - Ver perfil
- `/accounts/editar-perfil/` - Editar perfil

## 🔒 Permisos y Seguridad

- **Usuarios no autenticados** pueden:
  - Ver páginas, productos y clientes
  - Registrarse y hacer login
  - Acceder a "Acerca de mí"

- **Usuarios autenticados** pueden:
  - Todo lo anterior, más:
  - Crear, editar y eliminar páginas
  - Gestionar productos y clientes
  - Enviar y recibir mensajes
  - Editar su perfil

## 📝 Modelos Principales

### Page (Página/Blog)
- titulo: CharField
- subtitulo: CharField
- contenido: RichTextField (CKEditor)
- imagen: ImageField
- autor: ForeignKey(User)
- fecha_creacion, fecha_modificacion: DateTimeField

### Producto
- codigo_sku: CharField (primary key)
- nombre: CharField
- descripcion: TextField
- precio: DecimalField
- stock: PositiveIntegerField
- categoria: CharField (choices)
- imagen: ImageField

### Cliente
- id: UUIDField (primary key)
- nombre, apellido: CharField
- documento, telefono, domicilio: CharField
- tipo: CharField
- fecha_registro: DateTimeField

### ClienteCorporativo
- cliente: OneToOneField(Cliente)
- cuit: CharField
- razon_social: CharField
- nombre_fantasia: CharField

## 👨‍💻 Autor

**Sebastian Matías Hidalgo**

Proyecto Final - Curso de Python con Django - CoderHouse - 2025

## 📄 Licencia

Proyecto creado con fines educativos para el curso de Python de CoderHouse.


⭐ **¡Espero que disfrutes del proyecto!** ⭐

