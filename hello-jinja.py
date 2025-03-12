from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html',number=1995)

if __name__ == '__main__':
    app.run(debug=True, port=3000)