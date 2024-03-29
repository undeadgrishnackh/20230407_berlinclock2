import pytest
import responses
from requests import request

from modules import berlin_clock
from modules.berlin_clock import TimeFormatException, get_actual_time_from_worldtime_api
from tests.doubles.worldwide_time_api import stub_response_19_36_01


def describe_berlin_cloack_modules_composition_second_bulb_hours_minute():
    """📂 berlin clock modules integration - Seconds = 1 Bulb + Hours = 2 rows + Minutes = 2 rows"""

    def should_return_the_correct_string_for_the_berlin_clock_at_00_00_01_with_all_the_light_off():
        """🔌 should return the correct string for the berlin clock at 00:00:01 with all the light OFF:\n⬛️ \n⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️ \n⬛️⬛️⬛️⬛️"""
        assert berlin_clock.berlin_clock("00:00:01") == "O\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"

    def should_the_seconds_bulb_be_lit_at_00_00_02():
        """🔌 should the seconds bulb be lit 💡 at 00:00:02"""
        assert berlin_clock.berlin_clock("00:00:02") == "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"

    def should_the_first_hours_bottom_row_be_lit_in_red_at_01_00_00():
        """🔌 should the first hours bottom row be lit in red 🟥 at 01:00:01"""
        assert berlin_clock.berlin_clock("01:00:01") == "O\nOOOO\nROOO\nOOOOOOOOOOO\nOOOO"

    def should_the_first_light_of_top_and_bottom_rows_of_the_hours_be_lit_at_06_00_01():
        """🔌 should the first hours bottom row and the first hours top row be lit in red 🟥 at 06:00:01"""
        assert berlin_clock.berlin_clock("06:00:01") == "O\nROOO\nROOO\nOOOOOOOOOOO\nOOOO"

    def should_top_and_bottom_rows_of_the_minutes_be_completely_lit_yellow_and_red_at_00_59_01():
        """🔌 should the top and bottom rows of the minutes be completely lit in yellow 🟨 and red 🟥 at 00:59:01"""
        assert berlin_clock.berlin_clock("00:59:01") == "O\nOOOO\nOOOO\nYYRYYRYYRYY\nYYYY"


def describe_split_the_timestamp_in_hours_second_and_minutes():
    """📂 split the timestamp in hours, seconds, and minutes"""

    def should_split_the_time_in_hours_minutes_seconds():
        """🧪 should split the time in hours, minutes, seconds"""
        timestamp = "01:02:03"
        hours, minutes, seconds = berlin_clock.split_timestamp(timestamp)
        assert seconds == 3
        assert minutes == 2
        assert hours == 1

    def should_split_the_time_with_2_digits():
        """🧪 should split the time with 2 digits"""
        timestamp = "23:59:58"
        hours, minutes, seconds = berlin_clock.split_timestamp(timestamp)
        assert seconds == 58
        assert minutes == 59
        assert hours == 23


def describe_guardians_to_prevent_strange_time_coming_in():
    """📂 Guardians to prevent strange time coming in"""

    def should_raise_an_exception_if_the_time_isnt_a_string():
        """🧪 should raise an exception if the time isn't a string"""
        try:
            berlin_clock.berlin_clock(123)
            assert False
        except TimeFormatException as error_message:
            assert str(error_message) == "The time must be a string"

    wrong_timestamp = [
        ("123:00:00", "The time must be a string in the format 24HH:MM:ss"),
        ("23:62:00", "The time must be a string in the format 24HH:MM:ss"),
        ("12:00:99", "The time must be a string in the format 24HH:MM:ss"),
        ("HH:MM:ss", "The time must be a string in the format 24HH:MM:ss"),
    ]

    @pytest.mark.parametrize("timestamp,expected_error_message", wrong_timestamp)
    def should_raise_an_exception_if_the_time_isnt_in_the_format_hh_mm_ss(timestamp, expected_error_message):
        """🧪 should raise an exception if the time isn't in the format HH:MM:ss"""
        try:
            berlin_clock.berlin_clock(timestamp)
            assert False
        except TimeFormatException as error_message:
            assert str(error_message) == expected_error_message

    def should_get_the_time_from_worldtimeapi_if_the_user_doesnt_provide_it_fake_19_36_01(mocker):
        """🧪🎭 should get the time from WorldTimeApi if the user doesn't provide it. FAKE: 19:36.01"""
        timestamp = "19:36:01"
        stub_worldtime_api_json_reply = {
            "abbreviation": "CEST",
            "client_ip": "188.95.151.252",
            "datetime": "2023-09-01T19:36:01.940852+02:00",
            "day_of_week": 5,
            "day_of_year": 244,
            "dst": True,
            "dst_from": "2023-03-26T01:00:00+00:00",
            "dst_offset": 3600,
            "dst_until": "2023-10-29T01:00:00+00:00",
            "raw_offset": 3600,
            "timezone": "Europe/Berlin",
            "unixtime": 1693556553,
            "utc_datetime": "2023-09-01T08:22:33.940852+00:00",
            "utc_offset": "+02:00",
            "week_number": 35,
        }
        stub_datetime_from_json_reply = "2023-09-01T19:36:01.940852+02:00"
        expected_berlin_clock_time = "O\nRRRO\nRRRR\nYYRYYRYOOOO\nYOOO"

        # 1. check the time at 19:36:01 is "O\nRRRO\nRRRR\nYYRYYRYOOOO\nYOOO"
        assert berlin_clock.berlin_clock(timestamp) == expected_berlin_clock_time

        # get the time from the worldtimeapi  --- MOCK due to integration test!
        mocker.patch(
            "modules.berlin_clock.get_actual_time_from_worldtime_api", return_value=stub_worldtime_api_json_reply
        )
        assert berlin_clock.get_actual_time_from_worldtime_api() == stub_worldtime_api_json_reply

        # extract the datetime from all the fields of the json reply
        assert (
            berlin_clock.extract_datetime_from_json_reply(stub_worldtime_api_json_reply)
            == stub_datetime_from_json_reply
        )

        # extract the timestamp from the worldtimeapi reply at 19:36:01
        assert berlin_clock.extract_time_from_worldtimeapi_reply(stub_datetime_from_json_reply) == "19:36:01"

        # LAST. check at timestamp 19:36:01 that berlin clock WITHOUT PARAMS replies "O\nRRRO\nRRRR\nYYRYYRYOOOO\nYOOO"
        assert berlin_clock.berlin_clock("") == expected_berlin_clock_time

        # issues:
        # 1. an argument is always needed
        #    None, '', () >> ERROR
        # 2. we get the time from the API >> JSON
        #    E           modules.berlin_clock.TimeFormatException: The time must be a string in the format 24HH:MM:ss
        # 3. we need to parse the JSON and extract the time
        #    >> "19:36:01" >> berlin_clock.berlin_clock(FAKE_TIME)


@responses.activate
def test_get_the_json_back_from_the_worldwide_time_api_mocked():
    """🔌🎭 should get a mocked json back from the worldwide time api"""
    responses.add(stub_response_19_36_01)
    response = get_actual_time_from_worldtime_api()
    assert type(response) == dict
    assert response.get("datetime") == "2023-09-01T19:36:01.940852+02:00"
