from pydantic import BaseModel, EmailStr

# ---------- USER ----------

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# ---------- PRODUCT ----------

class ProductBase(BaseModel):
    name: str
    price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
