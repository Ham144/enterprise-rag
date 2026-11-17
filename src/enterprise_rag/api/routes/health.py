from fastapi import APIRouter

router = APIRouter(
    prefix="/api/health",
    tags=['Health']
)

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "enterprise-rag"
    }