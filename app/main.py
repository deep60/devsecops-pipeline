import subprocess
import sqlite3
import os

SECRET_KEY = ""
# Fake secrets that match real token patterns — TruffleHog WILL catch these
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890ab"   # GitHub PAT format
STRIPE_KEY   = "sk_live_aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"  # Stripe secret key format
SLACK_TOKEN  = "xoxb-123456789012-123456789012-aBcDeFgHiJkLmNoPqRsTuV"  # Slack bot token
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"

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
