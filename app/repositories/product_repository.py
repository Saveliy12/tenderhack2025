from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.models.product import Product
from app.services.schemas.product import ProductCreate, ProductUpdate


class ProductRepository:
    """Репозиторий для работы с продуктами"""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, product_data: ProductCreate) -> Product:
        """Создать новый продукт"""
        product = Product(**product_data.model_dump())
        self.db.add(product)  # добавляет объект в сессию (не сохраняет в БД)
        await self.db.flush() # отправляет INSERT в БД, но не коммитит транзакцию, коммит делает роут в routes/products.py через get_db()
        await self.db.refresh(product) # обновляет объект из БД (получает id, created_at)
        return product

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        """Получить продукт по ID"""
        result = await self.db.execute( # выполнение запроса
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none() # возвращает один объект или None

    async def get_all(
        self,
        limit: int = 100
    ) -> List[Product]:
        """Получить список продуктов с пагинацией"""
        result = await self.db.execute(
            select(Product)
            .limit(limit) # вернуть не более N записей
            .order_by(Product.created_at.desc()) # сортировка по дате создания (новые первыми)
        )
        return list(result.scalars().all()) # список результатов

    async def update(
        self,
        product_id: int,
        product_data: ProductUpdate
    ) -> Optional[Product]:
        """Обновить продукт"""
        # Получаем продукт
        product = await self.get_by_id(product_id)
        if not product:
            return None

        # Обновляем только переданные поля
        update_data = product_data.model_dump(exclude_unset=True) # только переданные поля (не None)
        if not update_data:
            return product

        await self.db.execute(
            update(Product)
            .where(Product.id == product_id)
            .values(**update_data)
        )
        await self.db.flush() # отправляет UPDATE в БД

        # Возвращаем обновленный продукт
        return await self.get_by_id(product_id) # возвращает обновленный объект

    async def delete(self, product_id: int) -> bool:
        """Удалить продукт"""
        product = await self.get_by_id(product_id) # проверка существования через get_by_id()
        if not product:
            return False

        await self.db.execute(
            delete(Product).where(Product.id == product_id)
        )
        await self.db.flush() # отправляет DELETE в БД
        return True # возвращает True при успехе, False если не найден

