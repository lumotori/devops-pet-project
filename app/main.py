from fastapi import FastAPI

app = FastAPI(title="DevOps Pet Project")


@app.get("/")
def read_root():
    return {"message": "Hello from my DevOps pet project!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
