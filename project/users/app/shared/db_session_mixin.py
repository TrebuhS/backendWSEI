from sqlalchemy.orm import Session


class DBSessionMixin:
    def __init__(
            self,
            db: Session
    ):
        self._db = db
