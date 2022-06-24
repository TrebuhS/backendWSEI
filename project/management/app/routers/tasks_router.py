from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv

from app.models.tasks.task_create import TaskCreate
from app.models.tasks.task_update import TaskUpdate
from app.models.users.user_details import User
from app.repositories.tasks_repository import TasksRepository
from app.services.tasks.tasks_service import TasksService
from app.db.db import get_db
from app.shared.decorators.auth_required import auth_current_user
from app.shared.service_result import handle_result

router = APIRouter()


def get_tasks_service(db: Session = Depends(get_db)):
    return TasksService(
        db,
        TasksRepository(db)
    )


@cbv(router)
class TasksRouter:

    __db: Session = Depends(get_db)
    __service: TasksService = Depends(get_tasks_service)

    @router.post("/")
    async def add_task(
            self,
            task: TaskCreate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.add_task(user.id, task)
        return handle_result(result)

    @router.put("/")
    async def update_task(
            self,
            task: TaskUpdate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.update_task(user.id, task)
        return handle_result(result)

    @router.get("/")
    async def get_tasks(
            self,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_tasks(user.id)
        return handle_result(result)

    @router.get("/{task_id}")
    async def get_task(
            self,
            task_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.get_task(user.id, task_id)
        return handle_result(result)

    @router.delete("/{task_id}")
    async def delete_task(
            self,
            task_id: int,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.remove_task(user.id, task_id)
        return handle_result(result)

    @router.put("/{task_id}/share")
    async def share_tasks(
            self,
            task: TaskUpdate,
            user: User = Depends(auth_current_user)
    ):
        result = self.__service.update_task(user.id, task)
        return handle_result(result)