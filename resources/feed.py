import json

from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from models import Post, db_session

post_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
}

class Feed(Resource):
    @marshal_with(post_fields)
    def get(self):
        """Returns the complete feed of posts."""
        feed = db_session.query(Post).all()
        return feed
    
    @marshal_with(post_fields)
    def post(self):
        """Creates a new post."""
        payload = request.get_json()
        new_post = Post(title=payload['title'], body=payload['body'])

        db_session.add(new_post)
        db_session.commit()

        return new_post, 201


class SinglePost(Resource):
    @marshal_with(post_fields)
    def get(self, post_id):
        """Returns the post identified by post_id."""
        post = db_session.query(Post).get(post_id)
        if not post:
            abort(404, message='Post does not exists')
        return post
    
    @marshal_with(post_fields)
    def put(self, post_id):
        """Edits the post identified by post_id."""
        post = db_session.query(Post).get(post_id)
        if not post:
            abort(404, message='Post does not exists')
        payload = request.get_json()
        post.title = payload['title']
        post.body = payload['body']

        db_session.commit()

        return post, 201
    
    def delete(self, post_id):
        """Removes the post identified by post_id."""
        post = db_session.query(Post).get(post_id)
        if not post:
            abort(404, message='Post does not exists')
        db_session.delete(post)
        db_session.commit()

        return {'message':'succesfuly deleted the post.'}
