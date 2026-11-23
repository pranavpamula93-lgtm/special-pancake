from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_items as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu_items"
)


@router.post("/", response_model=schema.MenuItems)
def create(menu_item: schema.MenuItemsCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, menu_item=menu_item)


@router.get("/", response_model=list[schema.MenuItems])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.MenuItems)
def read_one(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menu_item_id=menu_item_id)


@router.put("/{item_id}", response_model=schema.MenuItems)
def update(menu_item_id: int, menu_item: schema.MenuItemsUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, menu_item=menu_item, menu_item_id=menu_item_id)


@router.delete("/{item_id}")
def delete(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, menu_item_id=menu_item_id)