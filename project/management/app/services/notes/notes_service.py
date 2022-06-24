from sqlalchemy.orm import Session

from app.models.notes.note_create import NoteCreate
from app.models.notes.note_update import NoteUpdate
from app.repositories.notes_repository import NotesRepository
from app.services.notes.notes_exception import NoteException
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult


class NotesService(BaseService):
    def __init__(
            self,
            db: Session,
            notes_repository: NotesRepository
    ):
        super().__init__(db)
        self.__notes_repository = notes_repository

    def add_note(self, current_user_id: id, note: NoteCreate) -> ServiceResult:
        note = self.__notes_repository.add_note(current_user_id, note)
        return ServiceResult(note)

    def get_note(self, user_id: id, note_id: int) -> ServiceResult:
        note = self.__notes_repository.get_note(user_id, note_id)
        if not note:
            return ServiceResult(NoteException.NotFound())
        return ServiceResult(note)

    def get_notes(self, user_id: int):
        return self.__notes_repository.get_notes(user_id)

    def update_note(self, user_id: id, note: NoteUpdate) -> ServiceResult:
        note = self.__notes_repository.update_note(user_id, note)
        if not note:
            return ServiceResult(NoteException.NotFound())
        return ServiceResult(note)

    def remove_note(self, user_id: int, note_id: int):
        self.__notes_repository.delete_note(user_id, note_id)
        return ServiceResult(True)

