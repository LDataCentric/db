from typing import Optional, Any, Dict, Union
from sqlalchemy.sql import func

from db.business_objects import general
import db.enums as enums
from db.session import session
from db.models import (
    Model,
)


def get(model_id: str) -> Model:
    return (
        session.query(Model)
        .filter(
            Model.id == model_id,
        )
        .first()
    )


def get_all(project_id: str) -> list[Model]:
    return (
        session.query(Model)
        .filter(
            Model.project_id == project_id,
        )
        .all()
    )


def create(
    project_id: str,
    user_id: str,
    target_id: str,
    name: str,
    description: str,
    metric: str,
    algorithms: dict,
    active_algorithm: Optional[str] = None,
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> Model:

    model: Model = Model(
        project_id=project_id,
        user_id=user_id,
        target_id=target_id,
        name=name,
        description=description,
        metric=metric,
        algorithms=algorithms,
        active_algorithm=active_algorithm,
        created_at=created_at,
    )
    general.add(model, with_commit)
    return model


def delete(model_id: str, with_commit: bool = False) -> None:
    session.query(Model).filter(
        Model.id == model_id,
    ).delete()
    general.flush_or_commit(with_commit)


def update(
    model_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metric: Optional[str] = None,
    algorithms: Optional[dict] = None,
    active_algorithm: Optional[str] = None,
    with_commit: bool = False,
) -> Model:
    model: Model = session.query(Model).get(model_id)

    if name is not None:
        model.name = name

    if description is not None:
        model.description = description

    if metric is not None:
        model.metric = metric

    if algorithms is not None:
        model.algorithms = algorithms

    if active_algorithm is not None:
        model.active_algorithm = active_algorithm

    general.flush_or_commit(with_commit)
    return model
