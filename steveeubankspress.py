from flask import Flask, redirect, url_for, request,render_template
import pymongo
import os
import mongoconnectionsettings as mcs

app = Flask(__name__)

#string_f
connection = pymongo.MongoClient('mongodb://localhost',username=mcs.username, password=mcs.password,authSource=mcs.authSource)
db = connection.presssite

@app.route("/")
def index():

    _books = db.pubs.find({'type':'book'}).sort('published_date',pymongo.DESCENDING).limit(5)
    books = [book for book in _books]
    return render_template('home.html',books=books)

@app.route('/pubs')
def pubs():
    return "This is the page for all publications in the reverse order in which they were published."

if __name__=="__main__":
    app.run(host='0.0.0.0')
