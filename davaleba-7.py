from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    movie = {
        "movie": "😊✨🎬 movie is the best 🎬✨😊"
    }
    return render_template('index.html', movie=movie)

@app.route('/movie')
def movie():
    return render_template('movie.html')  # About page

@app.route('/actor')
def actor():
    return render_template('actor.html')
    
if __name__ == '__main__':
    app.run( debug=True )
