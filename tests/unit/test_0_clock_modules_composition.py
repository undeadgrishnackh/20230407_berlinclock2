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

    def should_light_the_top_and_botton_rows_of_the_hours_at_06_00_01():
        """🔌🧪🎭 should light the top and botton rows of the hours at 06:00:01"""
        assert (
            berlin_clock.berlin_clock("06:00:01") == "O\nROOO\nROOO\nOOOOOOOOOOO\nOOOO"
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
        """🧪 should be everything OFF in the BOTTOM row at 00:00:00"""
        assert berlin_clock.hours_bottom_row(0) == "OOOO"

    def should_light_the_hours_bottom_row_first_lamp_at_01_00_00():
        """🧪 should be 1 bulb in the BOTTOM row ON at 01:00:00"""
        assert berlin_clock.hours_bottom_row(1) == "ROOO"

    def should_be_2_bulbs_on_at_02_00_00():
        """🧪 should be 2 bulbs in the BOTTOM row ON at 02:00:00"""
        assert berlin_clock.hours_bottom_row(2) == "RROO"

    def should_be_4_bulbs_on_at_04_00_00():
        """🧪 should be 4 bulbs in the BOTTOM row ON at 04:00:00"""
        assert berlin_clock.hours_bottom_row(4) == "RRRR"

    def should_be_5_bulbs_on_at_05_00_00():
        """🧪 should be 0 bulb in the BOTTOM row ON at 05:00:00"""
        assert berlin_clock.hours_bottom_row(5) == "OOOO"

    def should_be_6_bulbs_on_at_06_00_00():
        """🧪 should be 0 bulb in the BOTTOM row ON at 06:00:00"""
        assert berlin_clock.hours_bottom_row(6) == "ROOO"

    def should_be_one_bulb_in_the_top_row_on_at_05_00_00():
        """🧪 should be 1 bulb in the TOP row ON at 05:00:00"""
        assert berlin_clock.hours_top_row(5) == "ROOO"

    def should_be_4_bulbs_in_the_top_row_on_at_20_00_00():
        """🧪 should be 4 bulbs in the TOP row ON at 20:00:00"""
        assert berlin_clock.hours_top_row(20) == "RRRR"


def describe_minutes_module():
    """📂 minutes module"""

    def should_be_1_light_on_in_the_bottom_row_of_the_minutes_at_00_01_01():
        """🧪 should be 1 light ON in the BOTTOM ROW of the minutes at 00:01:01"""
        assert berlin_clock.minutes_bottom_row(1) == "YOOO"

    def should_be_4_lights_on_in_the_bottom_row_of_minutes_at_00_04_01():
        """🧪 should be 4 lights ON in the BOTTOM ROW of minutes at 00:04:01"""
        assert berlin_clock.minutes_bottom_row(4) == "YYYY"

    def should_be_0_light_on_in_the_bottom_row_of_minutes_at_00_05_01():
        """🧪 should be 0 light ON in the BOTTOM ROW of minutes at 00:05:01"""
        assert berlin_clock.minutes_bottom_row(5) == "OOOO"

    def should_be_1_yellow_light_on_in_the_top_row_of_minutes_at_00_05_01():
        """🧪 should be 1 yellow light ON in the TOP ROW of minutes at 00:05:01"""
        assert berlin_clock.minutes_top_row(5) == "YOOOOOOOOOO"

    def should_be_2_yellow_lights_on_in_the_top_row_of_minutes_at_00_10_01():
        """🧪 should be 2 yellow light ON in the TOP ROW of minutes at 00:10:01"""
        assert berlin_clock.minutes_top_row(10) == "YYOOOOOOOOO"

    def should_be_2_yellow_lights_and_1_red_on_in_the_top_row_of_minutes_at_00_15_01():
        """🧪 should be 2 yellow light and 1 red ON in the TOP ROW of minutes at 00:15:01"""
        assert berlin_clock.minutes_top_row(15) == "YYROOOOOOOO"

    def should_be_2_yellow_lights_and_1_red_2_times_on_in_the_top_row_of_minutes_at_00_30_01():
        """🧪 should be 2 yellow light and 1 red for two times ON in the TOP ROW of minutes at 00:30:01"""
        assert berlin_clock.minutes_top_row(30) == "YYRYYROOOOO"

    def should_be_all_on_in_the_top_row_of_minutes_at_00_59_01():
        """🧪 should be all ON in the TOP ROW of minutes at 00:59:01"""
        assert berlin_clock.minutes_top_row(59) == "YYRYYRYYRYY"


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
