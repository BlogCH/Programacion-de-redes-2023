import json
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='1207',
        database='veterinaria_ch',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animales')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO animales(nombre, tipo, edad, color, fecha_nacimiento, ubicacion, observaciones) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert, (record['nombre'], record['tipo'], record['edad'], record['color'], record['fecha_nacimiento'], record['ubicacion'], record['observaciones']))
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM animales WHERE nombre = %s'
    cursor.execute(delete, (record['nombre'],))
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE animales SET edad = %s WHERE animal_id = %s'
    cursor.execute(update, (record['edad'], record['animal_id']))
    conn.commit()
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=True)


