from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm.session import Session

from ..auth import oauth2
from ..db_models.database import get_db
from ..db_models import models
from ..schemas import schemas
from ..schemas.item_schemas import ListOfItemOut, BaseItem, ItemOut
from app.controller.item import Item

router = APIRouter(
    prefix='/items',
    tags=['Item']

)

item = Item()


@router.get('/', response_model=ListOfItemOut)
def get_lists(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return item.get_item_lists(db=db)


@router.post("/", response_model=ItemOut)
def post_list(create_item: BaseItem, db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user)):
    return item.create_item(db=db, data=create_item)
#
#
# @router.get("/{id}")
# def get_post_by_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     post = db.query(db_models.Post).filter(db_models.Post.id == id).first()
#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
#     return post
#
#
# @router.put("/{id}", status_code=status.HTTP_200_OK)
# def update_list(id: int, updated_list: schemas.PostCreate, db: Session = Depends(get_db),
#                 current_user: int = Depends(oauth2.get_current_user)):
#     post_query = db.query(db_models.Post).filter(db_models.Post.id == id)
#     post = post_query.first()
#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
#     post_query.update(updated_list.dict(), synchronize_session=False)
#     db.commit()
#     return post_query.first()
#
#
# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_list(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     post_query = db.query(db_models.Post).filter(db_models.Post.id == id)
#     post = post_query.first()
#     if post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
#     post_query.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
