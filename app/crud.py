from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException


# CREATE
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


# READ ALL
def get_products(db: Session):
    return db.query(models.Product).all()


# READ ONE
def get_product(db: Session, product_id: int):
    product = db.query(models.Product)\
        .filter(models.Product.id == product_id)\
        .first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# UPDATE
def update_product(db: Session, product_id: int, data: schemas.ProductUpdate):

    product = get_product(db, product_id)

    for key, value in data.model_dump().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


# DELETE
def delete_product(db: Session, product_id: int):

    product = get_product(db, product_id)

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}
