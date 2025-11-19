from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.repositories.product_repository import ProductRepository
from app.services.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый продукт"
)
async def create_product(
    product_data: ProductCreate,
    db: AsyncSession = Depends(get_db)
):
    """Создать новый продукт"""
    repository = ProductRepository(db)
    product = await repository.create(product_data)
    return product


@router.get(
    "/",
    response_model=List[ProductResponse],
    summary="Получить список продуктов"
)
async def get_products(
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Получить список продуктов с пагинацией"""
    repository = ProductRepository(db)
    products = await repository.get_all(limit=limit)
    return products


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Получить продукт по ID"
)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Получить продукт по ID"""
    repository = ProductRepository(db)
    product = await repository.get_by_id(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Продукт с ID {product_id} не найден"
        )
    return product


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Обновить продукт"
)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Обновить продукт"""
    repository = ProductRepository(db)
    product = await repository.update(product_id, product_data)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Продукт с ID {product_id} не найден"
        )
    return product


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить продукт"
)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Удалить продукт"""
    repository = ProductRepository(db)
    deleted = await repository.delete(product_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Продукт с ID {product_id} не найден"
        )
    return None

