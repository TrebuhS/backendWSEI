from sqlalchemy.orm import Session

from app.db.tables.category import Category
from app.db.tables.task import Task
from app.models.tasks.task_create import TaskCreate
from app.models.tasks.task_update import TaskUpdate
from app.repositories.categories_repository import CategoriesRepository
from app.repositories.tags_repository import TagsRepository
from app.shared.base_crud import BaseCRUD


class TasksRepository(BaseCRUD):

    def __init__(
            self,
            db: Session,
            tags_repository: TagsRepository,
            categories_repository: CategoriesRepository
    ):
        super().__init__(db)
        self.__tags_repository = tags_repository
        self.__categories_repository = categories_repository

    def add_task(self, user_id: int, task: TaskCreate):
        new_task = Task(
            user_id=user_id,
            content=task.content
        )
        self._db.add(new_task)
        self._db.commit()
        self._db.refresh(new_task)

    def update_task(self, user_id: int, task: TaskUpdate):
        current_task = self.get_task(user_id, task.id)
        if not current_task:
            return None
        current_task.content = task.content
        current_task.tags = self.__tags_repository.get_tags_by_ids(task.tags_ids)
        current_task.category = self.__categories_repository.get_category(task.category_id)
        self._db.commit()
        self._db.refresh(current_task)

    def get_task(self, user_id: int, task_id: int) -> Task:
        return self._db.query(Task)\
            .filter(Task.user_id == user_id)\
            .filter(Task.id == task_id)\
            .first()

    def delete_task(self, user_id: int, task_id: int):
        self._db.query(Task)\
            .filter(Task.user_id == user_id)\
            .filter(Task.id == task_id)\
            .delete()
        self._db.commit()
