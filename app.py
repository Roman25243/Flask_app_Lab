from flask import Flask, Request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    agent = Request.user_agent
    return f"This is your homepage :) - {agent}"

@app.route('/user/<string:name>')
def greeting(name):
    name = name.upper()
    age = Request.args.get('age', 0, int)
    year = 2024 - age
    return f'Welcome, {name} - {year}', 200

@app.route('/admin')
def admin():
    to_url = url_for("greeting", name='administrator', _external=True)
    print(to_url)
    return redirect(to_url)

if __name__ == '__main__':
    app.run(debug=True)
