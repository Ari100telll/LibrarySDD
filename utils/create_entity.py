from http import HTTPStatus
from typing import Optional

from flask import jsonify

from resources import db


def create_entity(body: dict, model: db.Model, unique_field: Optional[str or None]):
    if unique_field is not None:
        duplicate_value = body.get(unique_field)
        already_exists = model.query.filter(
            model.__dict__[unique_field] == duplicate_value
        ).first()

        if already_exists:
            return {
                "err": f"{duplicate_value} is a duplicate value"
            }, HTTPStatus.BAD_REQUEST

    try:
        new_entity = model.from_dict(body)
        db.session.add(new_entity)
        db.session.commit()
        return jsonify(body), HTTPStatus.CREATED

    except Exception as e:
        return str(e)
