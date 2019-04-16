import json

from flask import Flask
from flask_restful import Api

from resources import Feed, SinglePost
from models.base import init_db, db_session

app = Flask(__name__)
api = Api(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(Feed, '/feed')
api.add_resource(SinglePost, '/feed/<string:post_id>')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
