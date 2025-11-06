from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/eason-music')
def eason_music_page():
    # 'eason_chan_music.html' have to be in folder templates
    return render_template('eason_chan_music.html')

if __name__ == '__main__':
    app.run(debug=True)
