from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    movie = request.form['movie']
    year = request.form['year']
    genre = request.form['genre']

    try:
        cursor.execute('INSERT INTO movies(movie, year, genre) VALUES (?,?,?)', (movie, year, genre))
        connection.commit()
        message = 'Successfully added your movie into the movie database.'
    except:
        connection.rollback()
        message = 'There was an issue adding your movie into the movie database.'
    finally:
        connection.close()
        return message

@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movieList = cursor.fetchall()
    connection.close()
    return jsonify(movieList)

app.run(debug = True)
