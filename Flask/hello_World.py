from flask import Flask

# __name__ tells the name of package where the class lies
app = Flask(__name__)

# decorator referrring to the root dir
@app.route('/')
def hello_world():
    return 'Hello World!'
