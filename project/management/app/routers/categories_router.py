from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.categories.category_create import CategoryCreate
from app.models.categories.category_details import Category
from app.models.users.user_details import User
from app.repositories.categories_repository import CategoriesRepository
from app.services.categories.categories_service import CategoriesService
from app.db.db import get_db
from app.shared.app_request import AppRequest
from app.shared.decorators.auth_required import auth_current_user
from app.shared.service_result import handle_result

router = APIRouter()


def get_categories_service(db: Session = Depends(get_db)):
    return CategoriesService(
        db,
        CategoriesRepository(db)
    )


@cbv(router)
class CategoriesRouter:

    __db: Session = Depends(get_db)
    __service: CategoriesService = Depends(get_categories_service)

    @router.post("/")
    async def add_category(
            self,
            category: CategoryCreate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.add_category(user.id, category)
        return handle_result(result)

    @router.get("/")
    async def get_categories(
            self,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_categories(user.id)
        return handle_result(result)

    @router.get("/{category_id}")
    async def get_category(
            self,
            category_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_category(user.id, category_id)
        return handle_result(result)

    @router.delete("/{category_id}")
    async def delete_category(
            self,
            category_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.remove_category(user.id, category_id)
        return handle_result(result)
