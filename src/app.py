from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        # Intentamos conectar a la base de datos MySQL usando las variables de entorno
        connection = pymysql.connect(
            host='db',
            user='root',
            password='rootpassword',
            database='test_db',
            cursorclass=pymysql.cursors.DictCursor
        )
        db_status = "¡Conexión exitosa a la Base de Datos MySQL! 🗄️"
    except Exception as e:
        db_status = f"Error al conectar a la BD: {e}"

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Docker + Python + MySQL</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f6f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
            .card {{ background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); text-align: center; max-width: 500px; }}
            h1 {{ color: #007bff; margin-bottom: 15px; }}
            p {{ color: #555; font-size: 16px; line-height: 1.5; }}
            .status {{ margin-top: 20px; padding: 10px; background: #e8f5e9; color: #2e7d32; border-radius: 8px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>¡Hola Mundo con Python y Docker! 🐳</h1>
            <p>Esta aplicación web se comunica internamente con un contenedor de MySQL.</p>
            <div class="status">{db_status}</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)