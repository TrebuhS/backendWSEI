from app.db.tables.tag import Tag
from app.models.tags.tag_create import TagCreate
from app.shared.base_crud import BaseCRUD


class TagsRepository(BaseCRUD):

    def add_tag(self, user_id: int, tag: TagCreate):
        new_tag = Tag(
            user_id=user_id,
            name=tag.name
        )
        self._db.add(new_tag)
        self._db.commit()
        self._db.refresh(new_tag)

    def get_tag(self, user_id: int, tag_id: int):
        return self._db.query(Tag)\
            .filter(Tag.user_id == user_id)\
            .filter(Tag.id == tag_id)\
            .first()

    def get_tags(self, user_id: int):
        return self._db.query(Tag)\
            .filter(Tag.user_id == user_id)\
            .all()

    def delete_tag(self, user_id: int, tag_id: int):
        self._db.query(Tag)\
            .filter(Tag.user_id == user_id)\
            .filter(Tag.id == tag_id)\
            .delete()
        self._db.commit()

    def get_tags_by_ids(self, user_id: int, tags_ids: [int]):
        return self._db.query(Tag)\
            .filter(Tag.user_id == user_id)\
            .filter(Tag.id.in_(tags_ids))\
            .all()
