from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.chat_router import router as chat_router
from page_router import router as page_router

app = FastAPI()

app.include_router(page_router)
app.include_router(chat_router)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
