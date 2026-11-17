
from fastapi import FastAPI
from enterprise_rag.api.routes import documents, health
import uvicorn

def create_app() -> FastAPI :
    app = FastAPI(
        title="rag enterprise",
        description="try to understand RAG structure enterprise",
        version="0.1.0"
    )
    app.include_router(health.router)
    app.include_router(documents.router)
    return app

app = create_app()

def run() -> None:
    uvicorn.run(app="enterprise_rag.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    run()