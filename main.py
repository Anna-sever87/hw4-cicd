from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет! Это моё приложение для ДЗ по CI/CD."}

@app.get("/time")
def get_time():
    return {"server_time": datetime.now().isoformat()}