# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  # Use a production server (e.g., Gunicorn) and turn off debug mode
  gunicorn_app = app
  gunicorn_app.run(host='0.0.0.0', port=5000, debug=False)

