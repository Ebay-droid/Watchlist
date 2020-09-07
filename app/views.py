from flask import render_template
from app import app

#Views
@app.route('/')
def index():
  '''
  view rootpage function that returns the index page and its data
  '''
  title ="Home - Welcome to the best Movie review website Online"
  return render_template('index.html', title = title)

@app.route('/movie/<movie_id>')
def movie(movie_id):
  return render_template('movie.html', id = movie_id)