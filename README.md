![Portada](/src/Portadas_Proyectos_GitHub.png)


# 🔷 API de Usuarios con Flask y MongoDB 🔷

### 🚀 Esta API de usuarios permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios en una base de datos MongoDB. Utiliza Flask para el desarrollo del servidor web y Flask-PyMongo para la interacción con MongoDB. 🚀

## Endpoints

### 1. 🏊‍♀️ Crear Usuario 🏊‍♀️

**URL:** `/users`  
**Método:** `POST`  
**Descripción:** Crea un nuevo usuario.

**Parámetros de Solicitud (JSON):**
```json
{
    "username": "nombre_usuario",
    "email": "correo@ejemplo.com",
    "password": "contrasena_segura"
}
```
### 2. 🤿🤿🤿 Obtener usuarios 🤿🤿🤿
**URL:** `/users`  
**Método:** `GET`  
**Descripción:** Obten la lista de usuarios registrados

### 3. 🤿 Obtener un solo usuario 🤿

**URL:** `/users/<user_id>`  
**Método:** `GET`  
**Descripción:** Obten los datos de un solo usuario.

### 4. 🖍️ Editar un usuario registrado 🖍️

**URL:** `/users/<user_id>`  
**Método:** `PUT`  
**Descripción:** Actualiza los datos de un usuario registrado

**Parámetros de Solicitud (JSON):**
```json
{
    "username": "nombre_usuario_actualizado",
    "email": "correo_actualizado@ejemplo.com",
}
```

### 5. 🗑️ Eliminar un usuario registrado 🗑️

**URL:** `/users/<user_id>`  
**Método:** `DELETE`  
**Descripción:** Elimina el usuario seleccionado
