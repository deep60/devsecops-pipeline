import subprocess
import sqlite3
import os

SECRET_KEY = ""
AWS_SECRET = ""

def get_user(username):
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    # SQL injection vulnerability — Semgrep will catch this
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def run_command(user_input):
    # Command injection vulnerability — Semgrep will catch this
    result = subprocess.run(user_input, shell=True, capture_output=True)
    return result.stdout

def read_file(path):
    # Path traversal vulnerability — Semgrep will catch this
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    print("App running...")
