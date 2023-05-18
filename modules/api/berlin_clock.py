from typing import Dict
from fastapi import FastAPI

from modules import berlin_clock

app = FastAPI()


@app.get("/berlin_clock")
def get_berlin_clock(timestamp: str) -> Dict:
    berlin_clock_string = berlin_clock.berlin_clock(timestamp)
    berlin_clock_lights = berlin_clock_string.split("\n")
    return {
        "time": timestamp,
        "seconds": berlin_clock_lights[0],
        "hours": {"top": berlin_clock_lights[1], "bottom": berlin_clock_lights[2]},
        "minutes": {"top": berlin_clock_lights[3], "bottom": berlin_clock_lights[4]},
    }
