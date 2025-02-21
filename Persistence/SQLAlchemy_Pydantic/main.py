from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud
import schemas.user
import schemas.post

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.user.UserResponse)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.user.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@app.get("/users/{email}", response_model=schemas.user.UserResponse)
def get_user(email: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db=db, email=email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_email(user_id: int, new_email: str, db: Session = Depends(get_db)):
    user = crud.update_user_email(db=db, user_id=user_id, new_email=new_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Email updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = crud.delete_user(db=db, user_id=user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@app.post("/posts/", response_model=schemas.post.PostResponse)
def create_post(post: schemas.post.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/users/{user_id}/posts", response_model=schemas.user.UserResponse)
def fetch_user_posts(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_with_posts(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
