from sqlalchemy.orm import Session
from model import User
from schemas import UserSchema
from exceptions import UserNotFound


def get_user(db: Session, skip: int = 0, limit=100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise UserNotFound
    return user


def create_user(db: Session, user: UserSchema):
    user = User(name=user.name, age=user.age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user_id: int, name: str, age: int):
    user = get_user_by_id(db=db, user_id=user_id)
    user.name = name
    user.age = age
    if not user:
        raise UserNotFound
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise UserNotFound
    db.delete(user)
    db.commit()