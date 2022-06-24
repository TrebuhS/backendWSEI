from app.db.tables.category import Category
from app.models.categories.category_create import CategoryCreate
from app.shared.base_crud import BaseCRUD


class CategoriesRepository(BaseCRUD):

    def add_category(self, user_id: int, category: CategoryCreate):
        new_category = Category(
            user_id=user_id,
            name=category.name
        )
        self._db.add(new_category)
        self._db.commit()
        self._db.refresh(new_category)

    def get_category(self, user_id: int, category_id: int):
        return self._db.query(Category)\
            .filter(Category.user_id == user_id)\
            .filter(Category.id == category_id)\
            .first()

    def get_categories(self, user_id: int):
        return self._db.query(Category)\
            .filter(Category.user_id == user_id)\
            .all()

    def delete_category(self, user_id: int, category_id: int):
        self._db.query(Category)\
            .filter(Category.user_id == user_id)\
            .filter(Category.id == category_id)\
            .delete()
        self._db.commit()
