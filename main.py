from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)

# Security flaw: Hardcoded credentials
DB_PATH = "database.db"

@app.route('/')
def home():
    return "Welcome to the DevSecOps Demo App!"

# Security flaw: SQL Injection vulnerability
@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username', '')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Unsafe query
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return str(user) if user else "User not found"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
