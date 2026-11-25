from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..dependencies.database import engine, get_db
from ..controllers import customers
from ..schemas import customers as schemas

router = APIRouter(
    tags=['Customers'],
    prefix="/customers",
    responses={404: {"description": "Not found"}},
)

# API Endpoints for Customers
@router.post("/", response_model= schemas.Customer, tags=["Customers"])
def create_customer(customer: schemas.Customer, db: Session = Depends(get_db)):
    return customers.create(db=db, request=customer)

@router.get("/", response_model= schemas.Customer, tags=["Customers"])
def get_customers(db: Session = Depends(get_db)):
    return customers.read_all(db=db)

@router.get("/{id}", response_model= schemas.Customer, tags=["Customers"])
def get_customer(id: int, db: Session = Depends(get_db)):
    return customers.read_one(id=id, db=db)

@router.delete("/{id}", response_model= schemas.Customer, tags=["Customers"])
def delete_customer(id: int, db: Session = Depends(get_db)):
    return customers.delete(id=id, db=db)

@router.post("/{customer_id}", response_model= schemas.Customer, tags=["Customers"])
def update_customer(customer_id: int, request: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    return customers.update(
        db=db,
        request=request,
        customer_id=customer_id
    )