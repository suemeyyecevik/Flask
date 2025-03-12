from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/hello')
def hello():
    return '<h1> Hello Page - path </h1>'

if __name__ == '__main__':
    app.run(debug=True, port=3000) 
    #port=3000
    # app.run(host= '0.0.0.0', port=8080)
