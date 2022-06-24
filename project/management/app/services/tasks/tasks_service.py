from sqlalchemy.orm import Session

from app.models.tasks.task_create import TaskCreate
from app.models.tasks.task_update import TaskUpdate
from app.repositories.tasks_repository import TasksRepository
from app.services.tasks.tasks_exception import TaskException
from app.shared.base_service import BaseService
from app.shared.service_result import ServiceResult


class TasksService(BaseService):
    def __init__(
            self,
            db: Session,
            tasks_repository: TasksRepository
    ):
        super().__init__(db)
        self.__tasks_repository = tasks_repository

    def add_task(self, current_user_id: id, task: TaskCreate) -> ServiceResult:
        task = self.__tasks_repository.add_task(current_user_id, task)
        return ServiceResult(task)

    def get_task(self, user_id: id, task_id: int) -> ServiceResult:
        task = self.__tasks_repository.get_task(user_id, task_id)
        if not task:
            return ServiceResult(TaskException.NotFound())
        return ServiceResult(task)

    def get_tasks(self, user_id: int):
        return self.__tasks_repository.get_tasks(user_id)

    def update_task(self, user_id: id, task: TaskUpdate) -> ServiceResult:
        task = self.__tasks_repository.update_task(user_id, task)
        if not task:
            return ServiceResult(TaskException.NotFound())
        return ServiceResult(task)

    def remove_task(self, user_id: int, task_id: int):
        self.__tasks_repository.delete_task(user_id, task_id)
        return ServiceResult(True)
