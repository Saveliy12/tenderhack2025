from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.conf import settings

engine = create_async_engine(
    settings.database_url,
    echo=settings.debug
)

SessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    autoflush=False
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    """Dependency для получения сессии БД"""
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
