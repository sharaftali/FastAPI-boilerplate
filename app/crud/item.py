from sqlalchemy.orm.session import Session
from app.db_models import models
from app.schemas.item_schemas import BaseItem


class Item:

    def get_lists(self, db: Session):
        return db.query(models.Item).all()

    def create_item(self, db: Session, data: BaseItem):
        new_item = models.Item(**data.dict())
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
