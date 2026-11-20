from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu_items

def create(db:Session, menu_item):
    db_menu_item = menu_item.MenuItems(
        dish = menu_item.dishes,
        ingredients = menu_item.ingredients,
        price = menu_item.price,
        calories = menu_item.calories,
        food_category = menu_item.food_category,
    )
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

def update(db:Session, menu_item_id, menu_item):
    db_menu_items = db.query(menu_items.MenuItems).filter(menu_items.MenuItems.id == menu_item_id)
    new_data = menu_item.model_dump(exclude_unset=True)
    db_menu_items.update(new_data, synchronize_session=False)
    db.commit()
    return db_menu_items.first()

def delete(db:Session, menu_item_id):
    db_menu_item = db.query(menu_items.MenuItems).filter(menu_items.MenuItems.id == menu_item_id)
    db_menu_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def read_all(db:Session):
    return db.query(menu_items.MenuItems).all()

def read_one(db: Session, menu_item_id):
    return db.query(menu_items.MenuItems).filter(menu_items.MenuItems.id == menu_item_id).first()
