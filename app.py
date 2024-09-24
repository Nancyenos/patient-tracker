from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Patient Tracker Application"

if __name__ == '__main__':
    app.run(debug=True)

