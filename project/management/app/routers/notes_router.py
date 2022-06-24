from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.notes.note_create import NoteCreate
from app.models.notes.note_update import NoteUpdate
from app.models.users.user_details import User
from app.repositories.notes_repository import NotesRepository
from app.services.notes.notes_service import NotesService
from app.db.db import get_db
from app.shared.decorators.auth_required import auth_current_user
from app.shared.service_result import handle_result

router = APIRouter()


def get_notes_service(db: Session = Depends(get_db)):
    return NotesService(
        db,
        NotesRepository(db)
    )


@cbv(router)
class NotesRouter:

    __db: Session = Depends(get_db)
    __service: NotesService = Depends(get_notes_service)

    @router.post("/")
    async def add_note(
            self,
            note: NoteCreate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.add_note(user.id, note)
        return handle_result(result)

    @router.put("/")
    async def update_note(
            self,
            note: NoteUpdate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.update_note(user.id, note)
        return handle_result(result)

    @router.get("/")
    async def get_notes(
            self,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_notes(0)
        return handle_result(result)

    @router.get("/{note_id}")
    async def get_note(
            self,
            note_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_note(user.id, note_id)
        return handle_result(result)

    @router.delete("/{note_id}")
    async def delete_note(
            self,
            note_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.remove_note(user.id, note_id)
        return handle_result(result)
