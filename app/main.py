from fastapi import FastAPI
from app.middleware import AuditLoggingMiddleware
from app.routes import router

app = FastAPI()
app.add_middleware(AuditLoggingMiddleware)
app.include_router(router)