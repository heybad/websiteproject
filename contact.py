from flask import render_template, request
import csv

def create_contact_routes(app, data_saver):
  @app.route('/contact', methods=['GET', 'POST'])
  def contact():
        result = None
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            data_saver.save_to_csv(first_name, last_name, email)
            result = "Data saved successfully!"
        return render_template('contact.html', result=result)
