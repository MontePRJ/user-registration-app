from flask import Flask, request, jsonify, render_template
import psycopg2
import os

app = Flask(__name__, template_folder="templates")


def get_db_connection():
    conn = psycopg2.connect(
        host="my-postgres",
        database="flaskdb",
        user="flaskuser",
        password="password"  # 👈 sostituire poi con os.environ.get('DB_PASSWORD')
    )
    return conn


@app.route('/')
def home():
    return render_template('index.html')


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
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
