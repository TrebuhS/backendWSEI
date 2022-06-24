from sqlalchemy.orm import Session

from app.db.tables.category import Category
from app.db.tables.note import Note
from app.models.categories.category_create import CategoryCreate
from app.models.notes.note_create import NoteCreate
from app.models.notes.note_update import NoteUpdate
from app.repositories.tags_repository import TagsRepository
from app.shared.base_crud import BaseCRUD


class NotesRepository(BaseCRUD):

    def __init__(self, db: Session, tags_repository: TagsRepository):
        super().__init__(db)
        self.__tags_repository = tags_repository

    def add_note(self, user_id: int, note: NoteCreate):
        new_note = Note(
            user_id=user_id,
            content=note.content
        )
        self._db.add(new_note)
        self._db.commit()
        self._db.refresh(new_note)

    def update_note(self, user_id: int, note: NoteUpdate):
        current_note = self.get_note(note.id)
        if current_note.user_id is not user_id:
            return None
        current_note.content = note.content
        current_note.tags = self.__tags_repository.get_tags_by_ids(note.tags)
        self._db.commit()
        self._db.refresh(current_note)

    def get_note(self, user_id: int, note_id: int) -> Note:
        return self._db.query(Note)\
            .filter(Note.user_id == user_id)\
            .filter(Note.id == note_id)\
            .first()

    def delete_note(self, note_id: int):
        self._db.query(Note).filter(Note.id == note_id).delete()
        self._db.commit()
