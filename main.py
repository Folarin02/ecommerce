from fastapi import FastAPI
from api import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
