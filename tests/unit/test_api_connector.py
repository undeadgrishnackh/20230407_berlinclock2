import inspect

import pytest
from fastapi import HTTPException

from modules.api import berlin_clock as api_connector


def describe_check_the_api_configuration():
    """📂 check the API configuration"""

    def should_know_the_api_version():
        """🧪 should know the API version is 1.0.0"""
        assert api_connector._API_VERSION == "1.0.0"

    def should_know_the_api_name():
        """🧪 should know the api name is getTime"""
        assert api_connector._API_NAME == "getTime"

    def should_know_the_name_of_the_api_parameter_is_timestamp():
        """🧪 should know the name of the api parameter is 'timestamp'"""
        signature = inspect.signature(api_connector.berlin_clock_api)
        api_parameter = list(signature.parameters.keys())
        assert "timestamp" in api_parameter, "The input parameter must be 'timestamp'"

    def should_know_the_type_of_the_api_parameter_is_string():
        """🧪 should know the type of the api parameter is 'string'"""
        signature = inspect.signature(api_connector.berlin_clock_api)
        api_parameter = list(signature.parameters.keys())
        api_parameter_info = signature.parameters["timestamp"]
        assert api_parameter_info.annotation == str, "'timestamp' must be annotated as a string"


def describe_the_api_connector_must_enforce_input_and_output_standards():
    """📂 the API connector must enforce input and output standards"""

    def should_check_the_string_converter_provides_the_right_json():
        """🧪 should check the string converter provides the right json"""
        expected_json = {
            "seconds": "Y",
            "hours": {"top": "RRRO", "bottom": "OOOO"},
            "minutes": {"top": "YYOOOOOOOOO", "bottom": "YYOO"},
        }
        well_formed_clock_string = "Y\nRRRO\nOOOO\nYYOOOOOOOOO\nYYOO"
        assert api_connector.convert_berlin_clock_string_into_json(well_formed_clock_string) == expected_json

    def should_block_a_wrong_berlin_clock_string_format_to_be_converted():
        """🧪 should block a wrong Berlin Clock string format to be converted"""
        expected_reply = {}
        bad_formed_clock_string = "bad_clock is time to BOOMMMMM"
        assert api_connector.convert_berlin_clock_string_into_json(bad_formed_clock_string) == expected_reply

    def should_block_non_input_string_to_be_converted():
        """🧪 should block NON input string to be converted"""
        expected_reply = {}
        wrong_input_format = {"12:!2:!2"}
        try:
            api_connector.convert_berlin_clock_string_into_json(wrong_input_format)
            assert False
        except TypeError as error:
            assert "expected string" in str(error)


def describe_component_test_to_ensure_the_api_connector_handles_200_and_400_reply_types():
    """📂 component test to ensure the api connector handles 200 and 400 reply types"""

    def should_expect_a_200_with_proper_json_time_at_12_34_56():
        """🧪 should expect a 200 with proper json time at 12:34:56"""
        assert api_connector.berlin_clock_api("12:34:56") == {
            "time": "12:34:56",
            "seconds": "Y",
            "hours": {"top": "RROO", "bottom": "RROO"},
            "minutes": {"top": "YYRYYROOOOO", "bottom": "YYYY"},
        }

    parameter_bad_timestamp_input = ["99:99:99", "Wrong_time", None, 123456]

    @pytest.mark.parametrize("bad_timestamp", parameter_bad_timestamp_input)
    def should_expect_a_400_as_http_exception_for_wrong_time_request(bad_timestamp):
        """🧪 should expect a 400 as HTTPException for wrong time request"""
        try:
            assert api_connector.berlin_clock_api(bad_timestamp)
            assert False
        except HTTPException as e:
            assert e.status_code == 400
            assert e.detail == "Invalid time format. Please provide the time in 24HH:MM:ss format."
