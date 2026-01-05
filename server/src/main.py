from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
import models
import schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

# initializing the API
app = FastAPI()

# Dependency to get a DB session per request
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_database)]
items = []

# create a REST API by defining endpoint & reading root
@app.get("/")
def read_root():
    return {"message": "Welcome to Boiler Gains!"}

# CRUD operations
@app.post("/items", response_model=schemas.ItemsBase)
def create_item(item: schemas.ItemsBase, db: db_dependency):
    db_item = models.Items(
        name=item.name,
        calories=item.calories,
        protein=item.protein,
        fats=item.fats,
        dining_hall_id=item.dining_hall_id
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=schemas.ItemsBase)
def get_item(item_id: int):
    
    
    if item_id < len(items): 
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=schemas.ItemsBase)
def update_item(item_id: int, item: schemas.ItemsBase):
    if item_id < len(items):
        items[item_id] = item
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=schemas.ItemsBase)
def delete_item(item_id: int):
    if item_id < len(items):
        deleted_item = items.pop(item_id)
        return deleted_item
    else:
        raise HTTPException(status_code=404, detail="Item not found")