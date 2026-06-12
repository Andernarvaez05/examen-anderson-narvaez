import os
import psycopg2
from flask import Flask, jsonify
 
app = Flask(__name__)
 
# ── Variables de entorno ──────────────────────────────────────────
APP_NAME    = os.getenv('APP_NAME',    'DevOps Examen App')
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
DB_HOST     = os.getenv('DB_HOST',     'localhost')
DB_NAME     = os.getenv('DB_NAME',     'examendb')
DB_USER     = os.getenv('DB_USER',     'examenuser')
DB_PASS     = os.getenv('DB_PASS',     'examenpass')
DB_PORT     = os.getenv('DB_PORT',     '5432')
 
def get_connection():
    return psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME,
        user=DB_USER, password=DB_PASS, port=DB_PORT
    )
 
def test_db():
    try:
        conn = get_connection()
        conn.close()
        return True
    except Exception:
        return False
 
# ── Ruta principal ────────────────────────────────────────────────
@app.route('/')
def index():
    db_ok = test_db()
    return jsonify({
        'app_name':   APP_NAME,
        'version':    APP_VERSION,
        'db_status':  'connected' if db_ok else 'error'
    })
 
# ── Ruta de productos ─────────────────────────────────────────────
@app.route('/productos')
def productos():
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('SELECT id, nombre, precio, stock FROM productos')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    result = [
        {'id': r[0], 'nombre': r[1],
         'precio': float(r[2]), 'stock': r[3]}
        for r in rows
    ]
    return jsonify(result)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
