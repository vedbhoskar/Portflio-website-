from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    email = request.form['email']
    name = request.form['name']
    contact_number = request.form['contact_number']

    contact_data = {
        'message': message,
        'email': email,
        'name': name,
        'contact_number': contact_number
    }

    with open('contacts.json', 'a') as file:
        json.dump(contact_data, file)
        file.write('\n')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0' )
