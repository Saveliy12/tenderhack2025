import sys
from pathlib import Path

# Добавляем корневую директорию проекта в PYTHONPATH
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import uvicorn
from fastapi import FastAPI

from app.routes import products

app = FastAPI(
    title="TenderHack API",
    description="API для работы с продуктами",
    version="1.0.0"
)

app.include_router(products.router)


@app.get("/")
async def root():
    """Корневой endpoint"""
    return {"message": "TenderHack API", "version": "1.0.0"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)