from fastapi import FastAPI

from api.v1.router import api_router
from core.config import settings
from core.container import Container


app = FastAPI(title=settings.PROJECT_NAME)

# set db and container
container = Container()
app.container = container
app.db = container.db()

app.include_router(api_router, prefix="/api/v1")
