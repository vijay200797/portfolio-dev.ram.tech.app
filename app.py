# app.py
from flask import Flask

app = Flask(__name__)  # Must be named 'app'

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

# REMOVE or wrap app.run(). Vercel will not load if app.run() blocks execution.
if __name__ == '__main__':
    app.run()