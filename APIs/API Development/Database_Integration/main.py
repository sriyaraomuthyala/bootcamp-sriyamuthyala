from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Item

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/")
def create_item(name: str, db: Session = Depends(get_db)):
    new_item = Item(name=name)
    db.add(new_item)
    db.commit()
    return {"message": "Item added", "item": name}
