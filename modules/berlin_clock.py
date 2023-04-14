# pylint: disable=C0321
def berlin_clock(timestamp: str):
    tokens = split_timestamp(timestamp)
    seconds = tokens.get("seconds")
    # minutes = tokens.get("minutes")
    hours = tokens.get("hours")
    return (
        f"{seconds_bulb(seconds)}\n"
        f"{hours_top_row(hours)}\n"
        f"{hours_bottom_row(hours)}\n"
        f"OOOOOOOOOOO\n"
        f"OOOO"
    )


def seconds_bulb(seconds: int):
    return "Y" if seconds % 2 == 0 else "O"


def hours_bottom_row(hours: int):
    return hours % 5 * "R" + (4 - hours % 5) * "O"


def hours_top_row(hours: int):
    return hours // 5 * "R" + (4 - hours // 5) * "O"


def split_timestamp(timestamp):
    return {
        "seconds": int(timestamp[-2:]),
        "minutes": int(timestamp[3:5]),
        "hours": int(timestamp[:2]),
    }


def minutes_bottom_row(minutes: int):
    return minutes % 5 * "Y" + (4 - minutes % 5) * "O"


def minutes_top_row(minutes: int):
    return minutes // 5 * "Y" + "OOOOOOOOOO"
