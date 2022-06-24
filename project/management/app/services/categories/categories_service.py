from sqlalchemy.orm import Session

from app.models.categories.category_create import CategoryCreate
from app.repositories.categories_repository import CategoriesRepository
from app.services.categories.categories_exception import CategoryException
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult


class CategoriesService(BaseService):
    def __init__(
            self,
            db: Session,
            categories_repository: CategoriesRepository
    ):
        super().__init__(db)
        self.__categories_repository = categories_repository

    def add_category(self, current_user_id: int, category: CategoryCreate) -> ServiceResult:
        category = self.__categories_repository.add_category(current_user_id, category)
        return ServiceResult(category)

    def get_category(self, user_id: int, category_id: int) -> ServiceResult:
        category = self.__categories_repository.get_category(user_id, category_id)
        if not category:
            return ServiceResult(CategoryException.NotFound())
        return ServiceResult(category)

    def get_categories(self, user_id: int):
        return self.__categories_repository.get_categories(user_id)

    def remove_category(self, user_id: int, category_id: int):
        self.__categories_repository.delete_category(user_id, category_id)
        return ServiceResult(True)
