from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    # category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    image_id = Column(String)
    category_path = Column(ARRAY(String))
    characteristics = Column(JSON)
    model = Column(String, nullable=False, index=True)
    code = Column(String, nullable=False, index=True)
    manufacturer = Column(String, nullable=False, index=True)
    last_category_name = Column(String, nullable=False, index=True)



# {
#     "id": 38885177,
#     "createdDate": "05.09.2025 06:59:28",
#     "productModel": "Kludi E2 492440575 для раковины",
#     "productCode": "01.11.01.04.05.01",
#     "productName": "Смеситель Kludi E2 492440575 для раковины",
#     "manufacturer": "KLUDI",
#     "price": null,
#     "description": null,
#     "lastCategoryName": "Смесители водоразборные",
#     "categoryPath": [
#         "1",
#         "72095647",
#         "793362869",
#         "793362891"
#     ],
#     "imageId": 231277051,
#     "characteristics": [
#         {
#             "id": 441795725,
#             "charName": "Комплектация",
#             "charUnit": null,
#             "charUnitName": null,
#             "charValue": "смеситель, инструкция"
#         }
#     ]
# }