from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.tags.tag_create import TagCreate
from app.models.users.user_details import User
from app.repositories.tags_repository import TagsRepository
from app.services.tags.tags_service import TagsService
from app.db.db import get_db
from app.shared.decorators.auth_required import auth_current_user
from app.shared.service_result import handle_result

router = APIRouter()


def get_tags_service(db: Session = Depends(get_db)):
    return TagsService(
        db,
        TagsRepository(db)
    )


@cbv(router)
class TagsRouter:

    __db: Session = Depends(get_db)
    __service: TagsService = Depends(get_tags_service)

    @router.post("/")
    async def add_tag(
            self,
            tag: TagCreate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.add_tag(user.id, tag)
        return handle_result(result)

    @router.get("/")
    async def get_tags(
            self,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_tags(user.id)
        return handle_result(result)

    @router.get("/{tag_id}")
    async def get_tag(
            self,
            tag_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_tag(user.id, tag_id)
        return handle_result(result)

    @router.delete("/{tag_id}")
    async def delete_tag(
            self,
            tag_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.remove_tag(user.id, tag_id)
        return handle_result(result)
