from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the CSV file
df_airlines = pd.read_csv('data/Airlines_data.csv')
df_loan = pd.read_csv('data/updated_loan.csv')
data_airlines = df_airlines.to_dict(orient='records')
data_loan = df_loan.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/home')
def home():
    return render_template('main.html') + render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/portfolio/airline')
def airline():
    return render_template('airline.html', data=data_airlines)

@app.route('/portfolio/scooter')
def scooter():
    return render_template('scooter.html', data=data_loan)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)






