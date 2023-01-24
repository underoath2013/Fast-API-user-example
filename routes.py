from fastapi import APIRouter, HTTPException, Path, Depends
from db_config import SessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema, RequestUser, Response
import crud
from sqlalchemy.orm import Session
from exceptions import UserNotFound

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    return Response(code=200, status="OK", message="Data created successfully").dict(exclude_none=True)


@router.get("/")
async def get(db: Session = Depends(get_db)):
    user = crud.get_user(db, 0, 100)
    return Response(code=200, status="OK", message="Successfully get all data", result=user).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_id(db, id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(code=200, status="OK", message="Successfully get data by id", result=user).dict(exclude_none=True)


@router.put("/{id}")
async def update_by_id(id: int, request: RequestUser, db: Session = Depends(get_db)):
    try:
        user = crud.update_user(
            db,
            user_id=id,
            name=request.parameter.name,
            age=request.parameter.age
        )
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(code=200, status="OK", message="Data updated successfully", result=user)


@router.delete("/{id}")
async def delete_by_id(id: int,  db: Session = Depends(get_db)):
    try:
        crud.delete_user(db, user_id=id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(code=200, status="OK", message="Successfully delete data by id").dict(exclude_none=True)

