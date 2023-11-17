from fastapi import FastAPI
from app.interaction import api as interaction_api
from app.message import api as message_api
from app.database import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

init_db()

app.include_router(interaction_api.router)
app.include_router(message_api.router)


# CORS middleware for handling Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

