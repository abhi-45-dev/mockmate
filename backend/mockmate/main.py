from fastapi import FastAPI

app = FastAPI(
    title="MockMate API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MockMate API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
