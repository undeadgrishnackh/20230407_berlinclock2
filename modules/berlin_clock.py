# pylint: disable=C0321
import re

from requests import request


def berlin_clock(timestamp: str) -> str:
    if timestamp == "":
        reply = get_actual_time_from_worldtime_api()
        datetime = extract_datetime_from_json_reply(reply)
        timestamp = extract_time_from_worldtimeapi_reply(datetime)

    check_timestamp(timestamp)
    hours, minutes, seconds = split_timestamp(timestamp)
    return (
        f"{seconds_bulb(seconds)}\n"
        f"{hours_top_row(hours)}\n"
        f"{hours_bottom_row(hours)}\n"
        f"{minutes_top_row(minutes)}\n"
        f"{minutes_bottom_row(minutes)}"
    )


def check_timestamp(timestamp):
    explode_if_not_a_string(timestamp)
    explode_if_wrong_time_format(timestamp)


def explode_if_wrong_time_format(timestamp):
    regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    pattern = re.compile(regex)
    if not re.search(pattern, timestamp):
        raise TimeFormatException("The time must be a string in the format 24HH:MM:ss")


def explode_if_not_a_string(timestamp):
    if not isinstance(timestamp, str):
        raise TimeFormatException("The time must be a string")


class TimeFormatException(Exception):
    """The time must be a string in the format HH:MM:SS - anything else is not allowed"""


def split_timestamp(timestamp):
    hours = int(timestamp[:2])
    minutes = int(timestamp[3:5])
    seconds = int(timestamp[-2:])
    return hours, minutes, seconds


def seconds_bulb(seconds: int):
    return "Y" if seconds % 2 == 0 else "O"


def hours_bottom_row(hours: int):
    return hours % 5 * "R" + (4 - hours % 5) * "O"


def hours_top_row(hours: int):
    return hours // 5 * "R" + (4 - hours // 5) * "O"


def minutes_bottom_row(minutes: int):
    return minutes % 5 * "Y" + (4 - minutes % 5) * "O"


def minutes_top_row(minutes: int):
    return (minutes // 5 * "Y" + (11 - minutes // 5) * "O").replace("YYY", "YYR", -1)


def extract_time_from_worldtimeapi_reply(json_reply: str) -> str:
    # response = request("http://worldtimeapi.org/api/timezone/Europe/Berlin")
    # datetime":"2023-09-01T10:22:33.940852+02:00",
    # if response.status_code == 200:
    #     return response.json()["datetime"]
    return json_reply[11:19]


def extract_datetime_from_json_reply(json_reply: dict) -> str:
    return json_reply.get("datetime")


def get_actual_time_from_worldtime_api():
    response = request(method="get", url="http://worldtimeapi.org/api/timezone/Europe/Berlin")
    return response.json() if response.status_code == 200 else {}
