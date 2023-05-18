from typing import Dict
from fastapi import FastAPI

app = FastAPI()


@app.get("/berlin_clock")
def get_berlin_clock(timestamp: str) -> Dict:
    return {"time": timestamp}
