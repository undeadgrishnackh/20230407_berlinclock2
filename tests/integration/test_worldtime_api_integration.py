from datetime import datetime

from modules import berlin_clock


def describe_integrate_with_the_worldtime_api():
    """📂 integrate with the WorldTime API"""

    def should_call_teh_api():
        """🔌🧪🎭 should call the real API and get the datetime starting with the actual date"""
        current_datetime = datetime.now()
        expected_date = current_datetime.strftime("%Y-%m-%d")
        response = berlin_clock.get_actual_time_from_worldtime_api()
        assert type(response) == dict
        assert response.get("datetime").startswith(expected_date)
