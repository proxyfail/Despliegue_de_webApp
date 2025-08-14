from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    database_url = os.environ.get('DATABASE_URL', 'URL de base de datos no configurada')
    return f'<h1>¡Hola, Papu!</h1><p>La URL de la base de datos es: {database_url}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)