from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="my-postgres",
        database="flaskdb",
        user="flaskuser",
        password="password"  # usa un Secret in produzione!
    )
    return conn

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    name = data.get('name')
    surname = data.get('surname')

    if not name or not surname:
        return jsonify({'error': 'Missing name or surname'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (
