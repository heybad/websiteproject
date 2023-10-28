from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the CSV file
df = pd.read_csv('Airlines_data.csv')

# Convert the DataFrame to a list of dictionaries for easy rendering in HTML
data = df.to_dict(orient='records')

@app.route('/')
def index():
    # Render 'main.html' and 'home.html'
    return render_template('main.html') + render_template('home.html')

@app.route('/portfolio')
def portfolio():
   return render_template('portfolio.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')
  
if __name__ == '__main__':
    gunicorn_app = app
    gunicorn_app.run(host='0.0.0.0', port=5000, debug=False)
