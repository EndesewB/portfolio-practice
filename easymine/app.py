from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample storage for user data
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    # Here, you should hash the password before saving it to the users list or database
    # For simplicity, I'm just saving it as is.
    users.append({'username': username, 'email': email, 'password': password})
    
    return jsonify({'message': 'User registered successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
