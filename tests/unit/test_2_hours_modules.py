from modules import berlin_clock


def describe_component_hours():
    """📂 component hours - 2 rows of 4 lamps each - Top one for 5 hours, bottom one for 1 hour - all red"""

    def should_be_everything_off_at_00_00_00():
        """🧪 should be everything OFF in the BOTTOM row ⚫⚫⚫⚫ at 00:00:00"""
        assert berlin_clock.hours_bottom_row(0) == "OOOO"

    def should_light_the_hours_bottom_row_first_lamp_at_01_00_00():
        """🧪 should be 1 bulb in the BOTTOM row ON 🔴⚫⚫⚫ at 01:00:00"""
        assert berlin_clock.hours_bottom_row(1) == "ROOO"

    def should_be_2_bulbs_on_at_02_00_00():
        """🧪 should be 2 bulbs in the BOTTOM row ON 🔴🔴⚫⚫ at 02:00:00"""
        assert berlin_clock.hours_bottom_row(2) == "RROO"

    def should_be_4_bulbs_on_at_04_00_00():
        """🧪 should be 4 bulbs in the BOTTOM row ON 🔴🔴🔴🔴 at 04:00:00"""
        assert berlin_clock.hours_bottom_row(4) == "RRRR"

    def should_be_5_bulbs_on_at_05_00_00():
        """🧪 should be 0 bulb in the BOTTOM row ON ⚫⚫⚫⚫at 05:00:00"""
        assert berlin_clock.hours_bottom_row(5) == "OOOO"

    def should_be_6_bulbs_on_at_06_00_00():
        """🧪 should be 0 bulb in the BOTTOM row ON ⚫⚫⚫⚫at 06:00:00"""
        assert berlin_clock.hours_bottom_row(6) == "ROOO"

    def should_be_one_bulb_in_the_top_row_on_at_05_00_00():
        """🧪 should be 1 bulb in the TOP row ON 🔴⚫⚫⚫at 05:00:00"""
        assert berlin_clock.hours_top_row(5) == "ROOO"

    def should_be_4_bulbs_in_the_top_row_on_at_20_00_00():
        """🧪 should be 4 bulbs in the TOP row ON 🔴🔴🔴🔴 at 20:00:00"""
        assert berlin_clock.hours_top_row(20) == "RRRR"
