from typing import Optional, Any, Dict, Union
from sqlalchemy.sql import func

from db.business_objects import general

import db.enums as enums
from db.session import session
from db.models import (
    Project,
    Layout,
)


def get(project_id: str, user_id: str, layout_type: str) -> Layout:
    return (
        session.query(Layout)
        .filter(
            Layout.project_id == project_id,
            Layout.layout_type == layout_type,
            Layout.user_id == user_id,
        )
        .first()
    )


def get_all(project_id: str, user_id: str, layout_type: str) -> list[Layout]:
    return (
        session.query(Layout)
        .filter(
            Layout.project_id == project_id,
            Layout.layout_type == layout_type,
            Layout.user_id == user_id,
        )
        .all()
    )


def create(
    project_id: str,
    user_id: str,
    name: str,
    layout_type: str,
    columns: dict,
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> Layout:

    layout: Layout = Layout(
        project_id=project_id,
        user_id=user_id,
        name=name,
        layout_type=layout_type,
        columns=columns,
        created_at=created_at,
    )
    general.add(layout, with_commit)
    return layout


def delete(layout_id: str, with_commit: bool = False) -> None:
    import time

    start_time = time.time()
    session.query(Layout).filter(
        Layout.id == layout_id,
    ).delete()
    general.flush_or_commit(with_commit)
    print("finished delete in", (time.time() - start_time))


def update(
    layout_id: str,
    name: Optional[str] = None,
    layout_type: Optional[str] = None,
    columns: Optional[dict] = None,
    with_commit: bool = False,
) -> Layout:
    layout: Layout = session.query(Layout).get(layout_id)

    if name is not None:
        layout.name = name

    if layout_type is not None:
        layout.layout_type = layout_type

    if columns is not None:
        layout.columns = columns

    general.flush_or_commit(with_commit)
    return layout
