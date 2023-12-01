from sqlalchemy.orm.session import Session
from app.schemas.item_schemas import ListOfItemOut, BaseItem, ItemOut
from app.crud.item import Item as CrudItem


class Item:
    def __init__(self):
        self.crud = CrudItem()

    def get_item_lists(self, db: Session) -> ListOfItemOut:
        return ListOfItemOut(items=self.crud.get_lists(db=db))

    def create_item(self, db: Session, data: BaseItem) -> ItemOut:
        return ItemOut(self.crud.create_item(db=db, data=data).__dict__)
