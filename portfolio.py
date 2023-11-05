from flask import render_template
from data_loader import load_data  # Import the data loader

# Load data outside of the route functions
data_airlines, data_loan = load_data()

def create_portfolio_routes(app):
    @app.route('/portfolio')
    def portfolio():
        return render_template('portfolio.html')

    @app.route('/portfolio/airline')
    def airline():
        return render_template('airline.html', data=data_airlines)

    @app.route('/portfolio/scooter')
    def scooter():
        return render_template('scooter.html', data=data_loan)
