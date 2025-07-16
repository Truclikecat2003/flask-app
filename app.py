from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    conn.close()

init_db()

@app.route("/")
def home():
    return "Flask app + SQLite chạy trên Render!"

@app.route("/add/<name>")
def add_user(name):
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return f"Đã thêm user: {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
