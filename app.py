# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-27 20:05:13
# @title:  Flask webiste url page

from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the sqlalchemy object
db = SQLAlchemy(app)

# import db schema
from models import *


def login_required(f):
    """login required decorator"""
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    try:
        posts = db.session.query(BlogPost).all()
    except Exception as e:
        print(e)
    return render_template('index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """route for handling the login page logic"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'sa':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You ware logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out!')
    return redirect(url_for('welcome'))


# def connect_db():
#     """connect the sqlite3 database"""
#     return sqlite3.connect('posts.db')


def main():
    # start the server with the 'run()' method
    app.run(debug=True)


if __name__ == '__main__':
    main()
