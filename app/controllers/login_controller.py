from http import HTTPStatus
from datetime import timedelta

from flask import request
from flask_jwt_extended import create_access_token

from app.models.user_model import User
from app.services.general_services import check_keys, check_keys_type
from app.exceptions.request_data_exceptions import (
    AttributeTypeError,
    MissingAttributeError,
)


def login():
    user_data = request.get_json()

    valid_keys = ["email", "password"]
    try:
        new_data = check_keys(user_data, valid_keys)
    except MissingAttributeError as m:
        return m.response, HTTPStatus.BAD_REQUEST

    try:
        check_keys_type(new_data, {"email": str, "password": str})
    except AttributeError as e:
        return e.response, HTTPStatus.BAD_REQUEST

    found_user = User.query.filter_by(email=new_data["email"]).first()
    if not found_user or not found_user.check_password(new_data["password"]):
        return {"error": "Invalid email or password."}, HTTPStatus.FORBIDDEN

    access_token = create_access_token(
        identity=found_user.id, expires_delta=timedelta(hours=1)
    )

    return {
        "name": found_user.name,
        "id": found_user.id,
        "access_token": access_token,
    }, HTTPStatus.OK
