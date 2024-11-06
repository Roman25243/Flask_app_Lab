from flask import  Flask, request, url_for, redirect, render_template, abort
from app import app
@app.route('/')
def main():
    return render_template ("base.html")

@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return render_template ("home.html", agent=agent )

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Моє резюме')