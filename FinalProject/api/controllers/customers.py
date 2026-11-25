from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers as models
from sqlalchemy.exc import SQLAlchemyError

# Create a new instance of the customers model with the given data
def create(db: Session, request):
    db_customer = models.Customers(
        customer_name=request.customer_name,
        email = request.email,
        phone_number = request.phone_number,
        address = request.address
    )

    # Add the newly created resource object to the database session
    db.add(db_customer)
    # Commit the changes to the database
    db.commit()
    # Refresh the resource object to ensure it reflects the current state in the database
    db.refresh(db_customer)
    # Return the newly created resource object
    return db_customer

# Update function
def update(db: Session, db_customer: models.Customers, request, customer_id):
    # Query the database for the specific resource to update
    db_customer = db.query(models.Customers).filter(models.Customers.id == customer_id)

    # Extract the update data from the provided 'resource' object
    update_data = request.model_dump(exclude_unset=True)

    # Update the database record with the new data, without synchronizing the session
    db_customer.update(update_data, synchronize_session=False)

    # Commit the changes to the database
    db.commit()

    # Return the updated resource record
    return db_customer.first()

# Delete function
def delete(db: Session, id: int):
    db_customer = db.query(models.Customers).filter(models.Customers.id == id)
    db_customer.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Read all function
def read_all(db: Session):
    return db.query(models.Customers).all()

# Read one function
def read_one(db: Session, id: int):
    return db.query(models.Customers).filter(models.Customers.id == id).first()