from typing import Optional, Any, Dict, Union
from sqlalchemy.sql import func

from db.business_objects import general
import db.enums as enums
from db.session import session
from db.models import (
    Training,
)

def get(training_id: str) -> Training:
    return (
        session.query(Training)
        .filter(
            Training.id == training_id,
        )
        .first()
    )


def get_all(model_id: str) -> list[Training]:
    return (
        session.query(Training)
        .filter(
            Training.model_id == model_id,
        )
        .all()
    )


def create(
    model_id: str,
    payload_id: str,
    algorithm: str,
    metrics: dict,
    statistics: dict,
    time: float,
    location: str,
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> Training:

    training: Training = Training(
        model_id=model_id,
        payload_id=payload_id,
        algorithm=algorithm,
        metrics=metrics,
        statistics=statistics,
        time=time,
        location=location,
        created_at=created_at,
    )
    general.add(training, with_commit)
    return training


def delete(training_id: str, with_commit: bool = False) -> None:
    session.query(Training).filter(
        Training.id == training_id,
    ).delete()
    general.flush_or_commit(with_commit)

