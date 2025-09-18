from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def home():
    current_user = session.get('user')
    return render_template('index.html', current_user=current_user)

@app.route('/info')
def info():
    return render_template('info.html')