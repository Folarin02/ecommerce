import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


class Product(BaseModel):
    name: str
    price: float
    description: str

products_db = []

@router.get("/products")
async def get_products():
    return products_db


@router.post("/products")
async def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product created successfully"}


@router.get("/products/{product_id}")
async def get_product(product_id: int):
    for product in products_db:
        if product_id == product_id:
            return product
    return {"message": "Product not found"}


@router.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    for idx, p in enumerate(products_db):
        if product_id == product_id:
            products_db[idx] = product
            return {"message": "Product updated successfully"}
    return {"message": "Product not found"}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for idx, product in enumerate(products_db):
        if product_id == product_id:
            products_db.pop(idx)
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}
