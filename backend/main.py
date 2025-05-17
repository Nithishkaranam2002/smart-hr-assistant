from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.query import router as query_router


app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the query route
app.include_router(query_router)

@app.get("/")
def root():
    return {"message": "Smart HR Assistant Backend is running "}
