from sqlalchemy.orm import Session

from app.models.categories.category_create import CategoryCreate
from app.models.tags.tag_create import TagCreate
from app.repositories.categories_repository import CategoriesRepository
from app.repositories.tags_repository import TagsRepository
from app.services.categories.categories_exception import CategoryException
from app.services.tags.tags_exception import TagException
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult


class TagsService(BaseService):
    def __init__(
            self,
            db: Session,
            tags_repository: TagsRepository
    ):
        super().__init__(db)
        self.__tags_repository = tags_repository

    def add_category(self, current_user_id: id, tag: TagCreate) -> ServiceResult:
        tag = self.__tags_repository.add_tag(current_user_id, tag)
        return ServiceResult(tag)

    def get_tag(self, user_id: id, tag_id: int) -> ServiceResult:
        tag = self.__tags_repository.get_tag(user_id, tag_id)
        if not tag:
            return ServiceResult(TagException.NotFound())
        return ServiceResult(tag)

    def remove_tag(self, user_id: int, tag_id: int):
        self.__tags_repository.delete_tag(user_id, tag_id)
        return ServiceResult(True)
