from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/posts/')
def posts():
    return render_template('posts/index.html')

@app.route('/test')
def test():
    return "Hello World"

if __name__ == '__main__':
    app.run()

