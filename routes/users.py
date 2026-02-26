from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, crud

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=schemas.Product)
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@router.get("/", response_model=list[schemas.Product])
def read_all(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.get("/{product_id}", response_model=schemas.Product)
def read_one(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)


@router.put("/{product_id}", response_model=schemas.Product)
def update(product_id: int, data: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, data)


@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)
