from flask import Flask
from controllers.tweets_controller import TweetsController
from controllers.middleware import Middleware
from db import Db


app = Flask(__name__)

#create database connection
db = Db()

#init controllers logic and pass db to it
tController = TweetsController(db)

app.wsgi_app = Middleware(app.wsgi_app)


# GET route to tweets
@app.route('/v1/tweets', methods = ['GET'])
def tweetsGet():
    return tController.tweetsGet()

# POST route to tweets
@app.route('/v1/tweets', methods = ['POST'])
def tweetsPost():
    return tController.tweetsPost()

# DELETE route to tweets
@app.route('/v1/tweets/<id>', methods = ['DELETE'])
def tweetsDelete(id):
    return tController.tweetsDelete(id)




if __name__ == '__main__':
    app.run(debug=True)