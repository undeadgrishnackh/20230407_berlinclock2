from modules import berlin_clock


def describe_component_seconds():
    """📂 Component Seconds - Lit on even, unlit on odd seconds"""

    def should_the_second_light_at_00():
        """🧪 should the second bulb lit 🟡 at 00 - even"""
        assert berlin_clock.seconds_bulb(0) == "Y"

    def should_the_seconds_bulb_be_off_at_00_00_01():
        """🧪 should the seconds bulb unlit ⚫️ at 00:00:01"""
        assert berlin_clock.seconds_bulb(1) == "O"

    def should_be_on_at_00_00_10():
        """🧪 should the seconds bulb lit 🟡 at 00:00:10"""
        assert berlin_clock.seconds_bulb(10) == "Y"
