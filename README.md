# Aplicación Web Hola Mundo con Python, Flask y MySQL (Docker Compose)

Repositorio para la práctica de integración de un servidor de aplicación web y una base de datos relacional orquestados mediante contenedores Docker.

## 🚀 Contenido del Proyecto
- **`src/app.py`**: Servidor web en Python con Flask que incluye lógica de reintentos automáticos para asegurar la conexión a la base de datos.
- **`src/requirements.txt`**: Archivo de dependencias (`Flask`, `pymysql`, `cryptography`).
- **`src/Dockerfile`**: Instrucciones para construir la imagen ligera de Python de la aplicación.
- **`docker-compose.yml`**: Archivo de orquestación que levanta tanto el servicio web (`app`) como el motor de base de datos (`db`) con volúmenes persistentes.

## ⚙️ Instrucciones de Ejecución
1. Clona este repositorio en tu computadora.
2. Asegúrate de tener **Docker** y **Docker Compose** instalados y ejecutándose.
3. En la raíz del proyecto, ejecuta el siguiente comando para construir y levantar los servicios:
   ```bash
   docker compose up --build -d
4. Abre tu navegador web e ingresa a: 
   ```bash
   http://localhost:5000