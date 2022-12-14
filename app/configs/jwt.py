import re
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager


def init_app(app: Flask):
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback(e, a):
        resp = {"error": "The token has expired"}

        return jsonify(resp), 401

    @jwt.unauthorized_loader
    def my_unauthorized_callback(e):
        resp = jsonify({"error": "Unauthorized"})

        return resp, 401

    @jwt.invalid_token_loader
    def my_invalid_token_loader_callback(e):
        msg = "Invalid token."
        status = 401
        search = re.search("Bad", e)

        if search:
            msg = "Missing authorization token"
            status = 401

        resp = jsonify({"error": msg})

        return resp, status
