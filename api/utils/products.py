from sqlalchemy.orm import Session

from db.model import products
from schemas.products import ProductCreate


def get_products(db: Session, product_id: int):
    return db.query(Product).filter(product.id == product_id).first()


def get_products(db: Session):
    return db.query(product).all()


def get_user_products(db: Session, user_id: int):
    courses = db.query(Product).filter(Product.user_id == user_id).all()
    return courses


def create_products(db: Session, product: ProductCreate):
    db_products = Product(
        title=product.title,
        description=product.description,
        user_id=product.user_id,
    )
    db.add(db_products)
    db.commit() 
    db.refresh(db_products)
    return db_products