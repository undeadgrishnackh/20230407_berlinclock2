import pytest

from modules import berlin_clock


def describe_berlin_cloack_modules_composition_second_bulb_hours_minute():
    """📂 berlin cloack modules composition: Second Bulb + 2 Hours rows + 2 Minutes rows"""

    def should_return_the_correct_string_for_the_berlin_clock_at_00_00_01_with_all_the_light_off():
        """🔌 should return the correct string for the berlin clock at 00:00:01 with all the light OFF"""
        assert (
            berlin_clock.berlin_clock("00:00:01") == "O\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"
        )

    def should_lit_the_seconds_bulb_at_00_00_02():
        """🔌 should light the seconds bulb at 00:00:02"""
        assert (
            berlin_clock.berlin_clock("00:00:02") == "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO"
        )

    def should_light_the_hours_at_01_00_00():
        """🔌 should light the hours at 01:00:00"""
        assert (
            berlin_clock.berlin_clock("01:00:01") == "O\nOOOO\nROOO\nOOOOOOOOOOO\nOOOO"
        )


def describe_component_seconds():
    """📂 Component_Seconds"""

    def should_the_second_light_at_00():
        """🧪 should the second bulb light at 00"""
        assert berlin_clock.seconds_bulb(0) == "Y"

    def should_the_seconds_bulb_be_off_at_00_00_01():
        """🧪 should the seconds bulb be OFF at 00:00:01"""
        assert berlin_clock.seconds_bulb(1) == "O"

    def should_be_on_at_00_00_10():
        """🧪 should be ON at 00:00:10"""
        assert berlin_clock.seconds_bulb(10) == "Y"


def describe_component_hours():
    """📂 component hours"""

    def should_be_everything_off_at_00_00_00():
        """🧪 should be everything off at 00:00:00"""
        assert berlin_clock.hours_bottom_row(0) == "OOOO"

    def should_light_the_hours_bottom_row_first_lamp_at_01_00_00():
        """🧪 should light the hours bottom row first lamp at 01:00:00"""
        assert berlin_clock.hours_bottom_row(1) == "ROOO"

    def should_be_2_bulbs_on_at_02_00_00():
        """🧪 should be 2 bulbs ON at 02:00:00"""
        assert berlin_clock.hours_bottom_row(2) == "RROO"

    def should_be_4_bulbs_on_at_04_00_00():
        """🧪 should be 4 bulbs ON at 04:00:00"""
        assert berlin_clock.hours_bottom_row(4) == "RRRR"

    def should_be_5_bulbs_on_at_05_00_00():
        """🧪 should be 0 bulb ON at 05:00:00"""
        assert berlin_clock.hours_bottom_row(5) == "OOOO"

    def should_be_6_bulbs_on_at_06_00_00():
        """🧪 should be 0 bulb ON at 06:00:00"""
        assert berlin_clock.hours_bottom_row(6) == "ROOO"


def describe_split_hte_timestamp_in_hours_second_and_minutes():
    """📂 split hte timestamp in hours, seconds, and minutes"""

    def should_split_the_time_in_hours_minutes_seconds():
        """🧪 should split the time in hours, minutes, seconds"""
        timestamp = "01:02:03"
        assert berlin_clock.split_timestamp(timestamp).get("seconds") == 3
        assert berlin_clock.split_timestamp(timestamp).get("minutes") == 2
        assert berlin_clock.split_timestamp(timestamp).get("hours") == 1

    def should_split_the_time_with_2_digits():
        """🧪 should split the time with 2 digits"""
        timestamp = "23:59:58"
        assert berlin_clock.split_timestamp(timestamp).get("seconds") == 58
        assert berlin_clock.split_timestamp(timestamp).get("minutes") == 59
        assert berlin_clock.split_timestamp(timestamp).get("hours") == 23
