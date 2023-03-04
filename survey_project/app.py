from flask import Flask, render_template, request
import sqlite3
import time

app = Flask(__name__)

@app.route('/')
def submit(): 
    message = request.form['message']
    add_message(message)

def add_message():
    




if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
