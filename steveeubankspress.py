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

#@app.route('/pubs')
#def pubs():
#    _publications = db.pubs.find({'type':'article'}).sort('published_date',pymongo.DESCENDING)
#    pubs = [pub for pub in _publications]

#    _books = db.pubs.find({'type':'book'}).sort('published_date',pymongo.DESCENDING)
#    books = [book for book in _books]

#    return render_template('pubs_list.html',pubs=pubs, books=books)



if __name__=="__main__":
    app.run(host='0.0.0.0')
