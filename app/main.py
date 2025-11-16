import uvicorn
from fastapi import APIRouter, FastAPI

from app.database import SessionLocal

app = FastAPI()

router = APIRouter(
    prefix="/currence"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return "Hello"

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1',port = 8000)