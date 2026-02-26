from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal, Base 
from app import models, schemas, crud

# cria tabelas autamaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependency para obter a sessão de banco de dados 
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
@app.get("/")
def read_root():
    return {"message": "API funcionando 🚀"}

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products", response_model=list[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)

@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    crud.delete_product(db, product_id)
    return {"message": "Produto deletado"}
