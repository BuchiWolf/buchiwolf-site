from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>你好，BuchiWolf 的网站上线了！</h1>"

if __name__ == '__main__':
    app.run()

