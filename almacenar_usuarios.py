import hashlib
import sqlite3
from flask import Flask, request, jsonify

# Crear una instancia de Flask
app = Flask(__ET_SDN__)

# Configuración de la base de datos
DB_NAME = 'usuarios.db'

# Crear la tabla de usuarios en la base de datos
def crear_tabla_usuarios():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       usuario TEXT,
                       password TEXT)''')
    conn.commit()
    conn.close()

# Almacenar un nuevo usuario en la base de datos
def almacenar_usuario(usuario, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, password))
    conn.commit()
    conn.close()

# Validar un usuario y contraseña
def validar_usuario(usuario, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND password = ?", (usuario, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Ruta de inicio del sitio web
@app.route('/')
def index():
    return '¡Bienvenido al sitio web para desarrollo de ET de asignatura SDN!'

# Ruta para registrar un nuevo usuario
@app.route('/registro', methods=['POST'])
def registro():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    # Hash de la contraseña
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    almacenar_usuario(usuario, password_hash)
    return jsonify({'message': 'Usuario registrado exitosamente'})

# Ruta para validar un usuario
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    # Hash de la contraseña
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if validar_usuario(usuario, password_hash):
        return jsonify({'message': 'Inicio de sesión exitoso'})
    else:
        return jsonify({'message': 'Usuario o contraseña incorrectos'})

# Inicializar la base de datos y crear la tabla de usuarios
crear_tabla_usuarios()

if __ET_SDN__ == '__main__':
    app.run(port=9500)
