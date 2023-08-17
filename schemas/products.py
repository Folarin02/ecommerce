from pydantic import BaseModel


class ProductBase(BaseModel):
    email: str


class ProductCreate(ProductBase):
    password: str


class Product(ProductBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

        