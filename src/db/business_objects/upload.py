from typing import List, Optional, Any, Dict, Union

from db.models import Upload
from db.session import session

from db.business_objects import general


def get(upload_id: str) -> Upload:
    return session.query(Upload).filter(Upload.id == upload_id).first()


def get_all(project_id: str) -> List[Upload]:
    return session.query(Upload).filter(Upload.project_id == project_id).all()


def create(
    project_id: str,
    name: str,
    user_id: str,
    location: Optional[str] = None,
    info: Optional[dict] = None,
    configuration: Optional[dict] = None,
    created_at: Optional[str] = None,
    with_commit: bool = False,
) -> Upload:

    upload: Upload = Upload(
        project_id=project_id,
        name=name,
        location=location,
        info=info,
        configuration=configuration,
        created_at=created_at,
        user_id=user_id,
    )
    general.add(upload, with_commit)
    return upload


def delete(upload_id: str, with_commit: bool = False) -> None:
    import time

    start_time = time.time()
    session.query(Upload).filter(
        Upload.id == upload_id,
    ).delete()
    general.flush_or_commit(with_commit)
    print("finished delete in", (time.time() - start_time))


def update(
    upload_id: str,
    name: Optional[str] = None,
    location: Optional[str] = None,
    info: Optional[dict] = None,
    configuration: Optional[dict] = None,
    with_commit: bool = False,
) -> Upload:
    upload: Upload = session.query(Upload).get(upload_id)

    if name is not None:
        upload.name = name

    if location is not None:
        upload.location = location

    if info is not None:
        upload.info = info

    if configuration is not None:
        upload.configuration = configuration

    general.flush_or_commit(with_commit)
    return upload
