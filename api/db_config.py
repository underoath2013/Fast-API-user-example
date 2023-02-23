from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

params = {
    "host":  os.getenv('POSTGRES_HOST', default='localhost'),
    "port": os.getenv('POSTGRES_PORT', default=5432),
    "database": os.getenv('POSTGRES_DB', default='users_db'),
    "user": os.getenv('POSTGRES_USER', default='postgres'),
    "password": os.getenv('POSTGRES_PASSWORD', default='password')
}

engine = create_engine(f'postgresql://{params["user"]}:{params["password"]}@{params["host"]}:{params["port"]}/{params["database"]}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

