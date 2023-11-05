from flask import Flask,request
import csv
from home import create_home_routes
from portfolio import create_portfolio_routes
from contact import create_contact_routes
from data_loader import load_data

app = Flask(__name__)

class DataSaver:
    def __init__(self, filename):
        self.filename = filename

    def save_to_csv(self, fname, lname, email):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([fname, lname, email])

data_saver = DataSaver('data.csv')

if __name__ == '__main__':
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Check if the file is empty before writing the header row
        if file.tell() == 0:
            writer.writerow(['first_name', 'last_name', 'email'])

# Create routes for home, portfolio, and contact
create_home_routes(app)
create_portfolio_routes(app)  # Pass data_saver as an argument
create_contact_routes(app, data_saver)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
