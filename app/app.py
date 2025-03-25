from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="my-postgres",
        database="flaskdb",
        user="flaskuser",
        password="password"  # Da usare solo in dev. In prod mettiamo un Secret.
    )
    return conn

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'name' not in data or 'surname' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    name = data['name']
    surname = data['surname']

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, surname) VALUES (%s, %s)", (name, surname))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'User registered'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT name, surname FROM users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
