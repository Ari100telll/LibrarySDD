from http import HTTPStatus

from flask import Response

from resources import db


def delete_entity(model: db.Model, entity_id: int):
    reader_category = model.query.get_or_404(entity_id)

    db.session.delete(reader_category)
    db.session.commit()
    return Response(status=HTTPStatus.NO_CONTENT)
