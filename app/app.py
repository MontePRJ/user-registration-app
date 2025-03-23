from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='my-postgres',
        database='flaskdb',
        user='flaskuser',
        password='password'  # Cambieremo poi con secret
    )
    return conn

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    surname = data.get('surname')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", (name, surname))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User registered'}), 201

@app.route('/users', methods=['GET'])
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, surname FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
