from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DokuAsk API is running"}