from flask import Flask, redirect, url_for, request,render_template
import pymongo
import os


app = Flask(__name__)

@app.route('/')
def spalsh_page():
    return render_template('splash.html')

@app.route("/home")
def index():
    return render_template('home.html')

@app.route('/books')
def books():
    return render_template('all_books.html')

if __name__=="__main__":
    app.run(host='0.0.0.0')
