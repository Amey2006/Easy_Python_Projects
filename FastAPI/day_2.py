from fastapi import FastAPI

app = FastAPI()

@app.get("/nav")
def home():
    return {"Name": "Binod"}

@app.get("/status")
def status():
    return {
        "server": "running",
        "attendance_system": "active"
    }