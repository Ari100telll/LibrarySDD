from flask import jsonify

from resources import db


def create_entity(body: dict, model: db.Model, unique_field: str):
    duplicate_value = body.get(unique_field)
    already_exists = model.query.filter(model.__dict__[unique_field] == duplicate_value).first()

    if already_exists:
        return {'err': f'{duplicate_value} is a duplicate value'}, 400

    try:
        new_entity = model.from_dict(body)
        db.session.add(new_entity)
        db.session.commit()
        return jsonify(body), 201

    except Exception as e:
        return str(e)
