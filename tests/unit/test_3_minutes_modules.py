from modules import berlin_clock


def describe_minutes_module():
    """📂 minutes module -- 2 rows - Top row has 11 lamps - Bottom row has 4 lamps"""

    def should_be_1_light_on_in_the_bottom_row_of_the_minutes_at_00_01_01():
        """🧪 should be 1 light ON in the BOTTOM ROW of the minutes 🟡⚫⚫⚫ at 00:01:01"""
        assert berlin_clock.minutes_bottom_row(1) == "YOOO"

    def should_be_4_lights_on_in_the_bottom_row_of_minutes_at_00_04_01():
        """🧪 should be 4 lights ON in the BOTTOM ROW of minutes 🟡🟡🟡🟡 at 00:04:01"""
        assert berlin_clock.minutes_bottom_row(4) == "YYYY"

    def should_be_0_light_on_in_the_bottom_row_of_minutes_at_00_05_01():
        """🧪 should be 0 light ON in the BOTTOM ROW of minutes ⚫⚫⚫⚫ at 00:05:01"""
        assert berlin_clock.minutes_bottom_row(5) == "OOOO"

    def should_be_1_yellow_light_on_in_the_top_row_of_minutes_at_00_05_01():
        """🧪 should be 1 yellow light ON in the TOP ROW of minutes 🟡⚫⚫⚫⚫⚫⚫⚫⚫⚫⚫ at 00:05:01"""
        assert berlin_clock.minutes_top_row(5) == "YOOOOOOOOOO"

    def should_be_2_yellow_lights_on_in_the_top_row_of_minutes_at_00_10_01():
        """🧪 should be 2 yellow light ON in the TOP ROW of minutes 🟡🟡⚫⚫⚫⚫⚫⚫⚫⚫⚫ at 00:10:01"""
        assert berlin_clock.minutes_top_row(10) == "YYOOOOOOOOO"

    def should_be_2_yellow_lights_and_1_red_on_in_the_top_row_of_minutes_at_00_15_01():
        """🧪 should be 2 yellow light and 1 red ON in the TOP ROW of minutes 🟡🟡🔴⚫⚫⚫⚫⚫⚫⚫⚫ at 00:15:01"""
        assert berlin_clock.minutes_top_row(15) == "YYROOOOOOOO"

    def should_be_2_yellow_lights_and_1_red_2_times_on_in_the_top_row_of_minutes_at_00_30_01():
        """🧪 should be 2 yellow light and 1 red for two times ON in the TOP ROW of minutes 🟡🟡🔴🟡🟡🔴⚫⚫⚫⚫⚫ at 00:30:01"""
        assert berlin_clock.minutes_top_row(30) == "YYRYYROOOOO"

    def should_be_all_on_in_the_top_row_of_minutes_at_00_59_01():
        """🧪 should be all ON in the TOP ROW of minutes 🟡🟡🔴🟡🟡🔴🟡🟡🔴🟡🟡 at 00:59:01"""
        assert berlin_clock.minutes_top_row(59) == "YYRYYRYYRYY"
