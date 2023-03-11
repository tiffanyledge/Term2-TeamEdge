from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import time

app = Flask(__name__)

@app.route('/')
def index():
    messages = final_message()
    
    return render_template('index.html', messages = messages)

@app.route('/edit/<rowid>')
def edit(rowid):
    message = get_message(rowid)
    return render_template('edit.html, message = message')

@app.route('/edit-message/<rowid>', methods = ['POST'])
def edit_message(rowid):
    message = request.form['message']
    update_message(message)

    return redirect(url_for('index'))

@app.route('/post-message', methods=['POST'])
def submit(): 
    message = request.form['message']
    add_message(message)
    messages = final_message()
    return render_template('index.html', messages = messages)
    # return redirect(url_for('index'))

@app.route('/delete-message/<rowid>')
def delete(rowid):
    delete_message(rowid)
    return redirect(url_for('index'))

def add_message(message):
    conn = sqlite3.connect('./static/data/message.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages(message) VALUES (?)", (message,))
    conn.commit()
    conn.close()

def update_message(message, rowid):
    conn = sqlite3.connect('./static/data/message.db')
    curs = conn.cursor()
    curs.execute("UPDATE messages SET message = ? WHERE rowid = ?", (message, rowid))
    conn.commit()
    conn.close()

def delete_message(rowid):
    conn = sqlite3.connect('./static/data/message.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM messages WHERE rowid = ?", (rowid,))
    conn.commit()
    conn.close()

def final_message():
    conn = sqlite3.connect('./static/data/message.db')
    curs = conn.cursor()
    result = curs.execute("SELECT rowid, * FROM messages")
    messages = []

    for row in result:
        message = {
            'message': row[1],
            'rowid': row[0]
        }
        messages.append(message)

    conn.close()
    return messages

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')