import pytest
from pytest_bdd import given, when, then, scenarios

import requests


def describe_contract_test_to_ensure_the_api_dictionary_is_as_expected():
    """📂 Contract test to ensure the API dictionary is as expected"""

    @pytest.fixture
    def response_berlin_clock_api_dictionary_v1_0_0():
        api_version = "1.0.0"
        api_name = "getTime"
        base_url_swagger_mock = (
            "https://virtserver.swaggerhub.com/undeadgrishnackh74/berlinClock"
        )
        parameter_name = "timestamp"
        timestamp = "13:56:01"
        return requests.get(
            f"{base_url_swagger_mock}/{api_version}/{api_name}?{parameter_name}={timestamp}"
        )

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
        assert json_data[0]["time"] == "13:56:01"
        assert json_data[0]["seconds"] == "Y"
        assert json_data[0]["hours"]["top"] == "RROO"
        assert json_data[0]["hours"]["bottom"] == "RRRO"
        assert json_data[0]["minutes"]["top"] == "YYRYYRYYRYY"
        assert json_data[0]["minutes"]["bottom"] == "YOOO"
