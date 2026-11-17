
from fastapi import APIRouter

from enterprise_rag.api.routes import health


api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])