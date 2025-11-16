import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.conf import settings

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/tenderhack"
engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, class_=AsyncSession)
Base = sqlalchemy.orm.declarative_base()

#     settings.database_url,
#     connect_args={"check_same_thread": False}
# )

# engine = create_engine(
#     settings.database_url,
#     connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def init_db():
#     Base.metadata.create_all(bind=engine)

