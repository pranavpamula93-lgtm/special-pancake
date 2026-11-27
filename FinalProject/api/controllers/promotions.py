from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promotions

def create(db:Session, promotion):
    db_promotion = promotions.Promotions(
        promo_code = promotion.promo_code,
        expiration_date = promotion.expiration_date
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def update(db:Session, promotion_id, promotion):
    db_promotion = db.query(promotions.Promotions).filter(promotions.Promotions.id == promotion_id)
    new_data = promotion.model_dump(exclude_unset=True)
    db_promotion.update(new_data, synchronize_session=False)
    db.commit()
    return db_promotion.first()

def delete(db:Session, promotion_id):
    db_promotion = db.query(promotions.Promotions).filter(promotions.Promotions.id == promotion_id)
    db_promotion.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def read_all(db:Session):
    return db.query(promotions.Promotions).all()

def read_one(db: Session, promotion_id):
    return db.query(promotions.Promotions).filter(promotions.Promotions.id == promotion_id).first()