from typing import Optional, Any, Dict, Union, List
from sqlalchemy.sql import func

from db.business_objects import general
import db.enums as enums
from db.session import session
from db.models import (
    ModelAttributes,
)


def get(model_attribute_id: str) -> ModelAttributes:
    return (
        session.query(ModelAttributes)
        .filter(
            ModelAttributes.id == model_attribute_id,
        )
        .first()
    )


def get_all(model_id: str) -> list[ModelAttributes]:
    return (
        session.query(ModelAttributes)
        .filter(
            ModelAttributes.model_id == model_id,
        )
        .all()
    )


def create(
    model_id: str,
    attribute_id: str,
    embedding_id: Optional[str] = None,
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> ModelAttributes:

    model_attributes: ModelAttributes = ModelAttributes(
        model_id=model_id,
        attribute_id=attribute_id,
        embedding_id=embedding_id,
        created_at=created_at,
    )
    general.add(model_attributes, with_commit)
    return model_attributes


def create_model_attributes(
    model_id: str,
    attributes: list[str],
    embeddings: dict = {},
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> List[ModelAttributes]:

    model_attributes = [
        ModelAttributes(
            model_id=model_id,
            attribute_id=attribute,
            created_at=created_at,
            embedding_id=embeddings.get(attribute),
        )
        for attribute in attributes
    ]
    general.add_all(model_attributes, with_commit)
    return model_attributes


def delete(model_attributes_id: str, with_commit: bool = False) -> None:
    session.query(ModelAttributes).filter(
        ModelAttributes.id == model_attributes_id,
    ).delete()
    general.flush_or_commit(with_commit)
