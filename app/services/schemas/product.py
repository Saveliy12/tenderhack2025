from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class ProductBase(BaseModel):
    """Базовая схема продукта"""
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    image_id: Optional[str] = None
    category_path: Optional[List[str]] = None
    characteristics: Optional[Dict[str, Any]] = None
    model: str
    code: str
    manufacturer: str
    last_category_name: str


class ProductCreate(ProductBase):
    """Схема для создания продукта"""
    pass


class ProductUpdate(BaseModel):
    """Схема для обновления продукта (все поля опциональные)"""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image_id: Optional[str] = None
    category_path: Optional[List[str]] = None
    characteristics: Optional[Dict[str, Any]] = None
    model: Optional[str] = None
    code: Optional[str] = None
    manufacturer: Optional[str] = None
    last_category_name: Optional[str] = None


class ProductResponse(ProductBase):
    """Схема для ответа API (включает id и created_at)"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

