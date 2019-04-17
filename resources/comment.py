import json

from flask import request
from flask_restful import Resource, abort, marshal_with, fields

from models import Post, Comment, db_session

comment_fields = {
    'id': fields.Integer,
    'post_id': fields.Integer,
    'body':fields.String,
    'created_at': fields.DateTime
}

class Comments(Resource):
    @marshal_with(comment_fields)
    def get(self, post_id):
        """Return the list of comments for a post"""
        post = db_session.query(Post).get(1)
        print(post)
        comments = db_session.query(Comment).filter(Comment.post_id==1).all()
        # comments = post.comments.all()
        print(comments)
        # comments = post.comments
        return comments

    @marshal_with(comment_fields)
    def post(self, post_id):
        """Save a comment for a specific post"""
        payload = request.get_json()
        new_comment = Comment(
            post_id=post_id,
            body=payload['body'],
            )
        db_session.add(new_comment)
        db_session.commit()
        return new_comment, 201

