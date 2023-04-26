from modules import berlin_clock


def describe_berlin_cloack_modules_composition_second_bulb_hours_minute():
    """📂 berlin clock modules integration - Seconds = 1 Bulb + Hours = 2 rows + Minutes = 2 rows"""

    def should_return_the_correct_string_for_the_berlin_clock_at_00_00_01_with_all_the_light_off():
        """🔌 should return the correct string for the berlin clock at 00:00:01 with all the light OFF:\nO\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"""
        assert (
            berlin_clock.berlin_clock("00:00:01") == "O\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"
        )

    def should_the_seconds_bulb_be_lit_at_00_00_02():
        """🔌 should the seconds bulb be lit 💡 at 00:00:02"""
        assert (
            berlin_clock.berlin_clock("00:00:02") == "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"
        )

    def should_the_first_hours_bottom_row_be_lit_in_red_at_01_00_00():
        """🔌 should the first hours bottom row be lit in red 🔴 at 01:00:01"""
        assert (
            berlin_clock.berlin_clock("01:00:01") == "O\nOOOO\nROOO\nOOOOOOOOOOO\nOOOO"
        )

    def should_the_first_light_of_top_and_bottom_rows_of_the_hours_be_lit_at_06_00_01():
        """🔌 should the first hours bottom row and the first hours top row be lit in red 🔴 at 06:00:01"""
        assert (
            berlin_clock.berlin_clock("06:00:01") == "O\nROOO\nROOO\nOOOOOOOOOOO\nOOOO"
        )

    def should_top_and_bottom_rows_of_the_minutes_be_completely_lit_yellow_and_red_at_00_59_01():
        """🔌 should the top and bottom rows of the minutes be completely lit in yellow 🟡 and red 🔴 at 00:59:01"""
        assert (
            berlin_clock.berlin_clock("00:59:01") == "O\nOOOO\nOOOO\nYYRYYRYYRYY\nYYYY"
        )


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
