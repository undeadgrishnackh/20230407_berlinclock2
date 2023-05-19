import re
from typing import Dict
from fastapi import FastAPI, HTTPException

from modules import berlin_clock
from modules.berlin_clock import TimeFormatException

app = FastAPI()


@app.get("/getTime")
def berlin_clock_api(timestamp: str) -> Dict:
    try:
        return {"time": timestamp, **convert_berlin_clock_string_into_json(berlin_clock.berlin_clock(timestamp))}
    except TimeFormatException as exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid time format. Please provide the time in 24HH:MM:ss format.",
        ) from exception


def convert_berlin_clock_string_into_json(berlin_clock_string: str) -> Dict:
    if the_berlin_clock_string_is_valid(berlin_clock_string):
        berlin_clock_lights = berlin_clock_string.split("\n")
        return {
            "seconds": berlin_clock_lights[0],
            "hours": {"top": berlin_clock_lights[1], "bottom": berlin_clock_lights[2]},
            "minutes": {"top": berlin_clock_lights[3], "bottom": berlin_clock_lights[4]},
        }
    return {}


def the_berlin_clock_string_is_valid(berlin_clock_string: str) -> bool:
    # if not isinstance(berlin_clock_string, str):
    #     return None
    regex = "^[YO]\\n([RO]{4})\\n([RO]{4})\\n([YO]{2}[RO][YO]{2}[RO][YO]{2}[RO][YO]{2})\\n([YO]{4})$"
    pattern = re.compile(regex)
    return bool(re.search(pattern, berlin_clock_string))
