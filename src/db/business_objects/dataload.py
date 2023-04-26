from typing import Optional, Any, Dict, Union
from sqlalchemy.sql import func

from db.business_objects import general
import db.enums as enums
from db.session import session
from db.models import (
    Dataload,
)


def get_dataload(dataload_id: str) -> Dataload:
    return (
        session.query(Dataload)
        .filter(
            Dataload.id == dataload_id,
        )
        .first()
    )


def get_all(model_id: str) -> list[Dataload]:
    return (
        session.query(Dataload)
        .filter(
            Dataload.model_id == model_id,
        )
        .all()
    )


def update_dataload(
    dataload_id: str,
    location: Optional[str] = None,
    with_commit: bool = False,
) -> Dataload:
    dataload: Dataload = session.query(Dataload).get(dataload_id)

    if location is not None:
        dataload.location = location

    general.flush_or_commit(with_commit)
    return dataload


def create_dataload(
    model_id: str,
    location: Optional[str] = None,
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> Dataload:

    dataload: Dataload = Dataload(
        location=location,
        model_id=model_id,
        created_at=created_at,
    )
    general.add(dataload, with_commit)
    return dataload


def delete_dataload(dataload_id: str, with_commit: bool = False) -> None:
    session.query(Dataload).filter(
        Dataload.id == dataload_id,
    ).delete()
    general.flush_or_commit(with_commit)
