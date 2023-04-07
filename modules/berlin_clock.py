# pylint: disable=C0321
def berlin_clock(timestamp: str):
    tokens = split_timestamp(timestamp)
    seconds = tokens.get("seconds")
    # minutes = tokens.get("minutes")
    hours = tokens.get("hours")
    return (
        f"{seconds_bulb(seconds)}\nOOOO\n{hours_bottom_row(hours)}\nOOOOOOOOOOO\nOOOO"
    )


def seconds_bulb(seconds: int):
    return "Y" if seconds % 2 == 0 else "O"


def hours_bottom_row(hours: int):
    return hours % 5 * "R" + (4 - hours % 5) * "O"


def split_timestamp(timestamp):
    return {
        "seconds": int(timestamp[-2:]),
        "minutes": int(timestamp[3:5]),
        "hours": int(timestamp[:2]),
    }
