from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from werkzeug.utils import secure_filename

# Create a Flask app instance
app = Flask(__name__)

# Set a secret key for flash messages (used to show alerts to the user)
app.secret_key = "supersecretkey"

# Function to connect to the SQLite Database
def get_db_connection():
    # Connect to 'musicreview.db' database.
    conn = sqlite3.connect('musicreview.db')
    # This makes it easier to access rows as dictonaries and the data by field
    # heading rather than by numbers
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Route to view all songs
@app.route('/songs')
def all_songs():
    # Render the 'all_songs.html' template and display it in the browser
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM songs")
    songs = cursor.fetchall()
    conn.close()
    return render_template('all_songs.html', songs = songs)

@app.route('/rate')
def song_rating():
    conn = get_db_connection()
    cursor = conn.cursor()
    conn.execute('SELECT * FROM songs WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('')

@app.route('/ratings')
def view_ratings():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users-ratings")
    ratings = cursor.fetchall()
    conn.close()
    return render_template('view_ratings.html', ratings = ratings)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 