from flask import render_template

def create_home_routes(app):
    @app.route('/')
    def index():
        return render_template('main.html')

    @app.route('/home')
    def home():
        return render_template('main.html') + render_template('home.html')
