from flask import Flask, Blueprint, render_template

# Define the blueprint for the index route
index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html', current_route='index')

@index_bp.route('/login')
def login():
    return render_template('login.html', current_route='login')
