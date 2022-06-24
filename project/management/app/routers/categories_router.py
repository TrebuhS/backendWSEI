from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.categories.category_create import CategoryCreate
from app.models.categories.category_details import Category
from app.repositories.categories_repository import CategoriesRepository
from app.services.categories.categories_service import CategoriesService
from app.db.db import get_db
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
            category: CategoryCreate
    ):
        result = self.__service.add_category(0, category)
        return handle_result(result)

    @router.get("/")
    async def get_categories(
            self
    ):
        result = self.__service.get_categories(0)
        return handle_result(result)
