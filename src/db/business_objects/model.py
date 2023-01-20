from datetime import datetime
from typing import Dict, List, Any, Optional

import db.enums as enums

from db.business_objects import general
from db.models import Model
from db.session import session


def get(model_id: str) -> Model:
    return (
        session.query(Model)
        .filter(
            Model.id == model_id,
        )
        .first()
    )

def get_models_by_information_source(information_source_id: str) -> List[Model]:
    return (
        session.query(Model)
        .filter(
            Model.information_source_id == information_source_id,
        )
        .all()
    )

def create(information_source_id: str,
    name: str,
    pycaret_type: str,
    version: int,
    metrics: dict,
    time: float,
    location: str,
    created_at: Optional[str] = None,
    with_commit: bool = False,) -> Model:
    model: Model = Model(
        information_source_id=information_source_id,
        name=name,
        pycaret_type=pycaret_type,
        version=version,
        metrics=metrics,
        time=time,
        location=location,
        created_at=created_at or datetime.now(),
    )
    general.add(model, with_commit)
    return model

