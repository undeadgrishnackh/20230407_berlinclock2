import pytest

import requests

from modules.api import berlin_clock

timestamp = "13:56:01"


def describe_contract_test_to_ensure_the_api_dictionary_is_as_expected():
    """📂 Contract test to ensure the API dictionary is as expected"""

    @pytest.fixture
    def response_berlin_clock_api_dictionary_v1_0_0():
        api_version = "1.0.0"
        api_name = "getTime"
        base_url_swagger_mock = "https://virtserver.swaggerhub.com/undeadgrishnackh74/berlinClock"
        parameter_name = "timestamp"
        return requests.get(f"{base_url_swagger_mock}/{api_version}/{api_name}?{parameter_name}={timestamp}")

    def should_find_the_api_dictionary_definition_for_the_get_time_v1_0_0(
        response_berlin_clock_api_dictionary_v1_0_0,
    ):
        """🔌🎭 should find the API dictionary definition for the getTime V1.0.0"""
        assert response_berlin_clock_api_dictionary_v1_0_0.status_code == 200

    def should_find_the_right_json_schema_for_the_berlin_clock_get_time_v_1_0_0(
        response_berlin_clock_api_dictionary_v1_0_0,
    ):
        """🔌🎭 should find the right JSON schema for the berlin clock get time ver. 1.0.0"""
        json_data = response_berlin_clock_api_dictionary_v1_0_0.json()
        assert json_data["time"] == "13:56:01"
        assert json_data["seconds"] == "O"
        assert json_data["hours"]["top"] == "RROO"
        assert json_data["hours"]["bottom"] == "RRRO"
        assert json_data["minutes"]["top"] == "YYRYYRYYRYY"
        assert json_data["minutes"]["bottom"] == "YOOO"


def describe_contract_test_to_ensure_that_the_api_developed_is_like_the_contract_above():
    """📂 contract test to ensure that the API developed is like the OPEN API specs"""

    def should_find_the_same_reply_as_for_the_berlin_clock_get_time_v_1_0_0_contract():
        """🔌🎭 should find the right JSON schema for the berlin clock get time ver. 1.0.0"""
        response_berlin_clock_api = berlin_clock.berlin_clock_api(timestamp)
        assert response_berlin_clock_api.get("time") == "13:56:01"
        assert response_berlin_clock_api.get("seconds") == "O"
        assert response_berlin_clock_api.get("hours").get("top") == "RROO"
        assert response_berlin_clock_api.get("hours").get("bottom") == "RRRO"
        assert response_berlin_clock_api.get("minutes").get("top") == "YYRYYRYYRYY"
        assert response_berlin_clock_api.get("minutes").get("bottom") == "YOOO"


def describe_integration_test_to_ensure_the_api_exposed_on_localhost_is_the_same_as_in_the_contract_above():
    """📂 integration test to ensure the API exposed on localhost is the same as in the OPEN API specs"""

    def should_call_the_api_on_localhost_as_for_the_contract_ver_1_0_0():
        """🔌 should call the api on localhost as for the contract ver. 1.0.0"""

        # launch the api in the background

        # curl the API

        # check the reply
