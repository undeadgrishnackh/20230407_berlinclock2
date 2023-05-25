import os
import signal
import socket
import subprocess
import time

import pytest
import requests

from modules.api import berlin_clock

api_version = "1.0.0"
api_name = "getTime"
parameter_name = "timestamp"
timestamp = "13:56:01"


expected_time_in_json_payload = "13:56:01"
expected_seconds_in_json_payload = "O"
expected_hours_top_in_json_payload = "RROO"
expected_hours_bottom_in_json_payload = "RRRO"
expected_minutes_top_in_json_payload = "YYRYYRYYRYY"
expected_minutes_bottom_in_json_payload = "YOOO"


def describe_contract_test_to_ensure_the_api_dictionary_is_as_expected():
    """📂 Contract test to ensure the API dictionary and the developed one are compliant to the contract"""

    @pytest.fixture
    def swagger_hub_mock_v1_0_0():
        base_url_swagger_mock = "https://virtserver.swaggerhub.com/undeadgrishnackh74/berlinClock"
        return requests.get(f"{base_url_swagger_mock}/{api_version}/{api_name}?{parameter_name}={timestamp}")

    def should_find_the_api_dictionary_definition_for_the_get_time_v1_0_0(
        swagger_hub_mock_v1_0_0,
    ):
        """🔌🎭 should find the API dictionary definition for the getTime V1.0.0"""
        assert swagger_hub_mock_v1_0_0.status_code == 200

    def should_find_the_right_json_schema_for_the_berlin_clock_get_time_v_1_0_0(
        swagger_hub_mock_v1_0_0,
    ):
        """🔌🎭 should find the mock api on SwaggerHub has the right JSON schema for the berlin clock get_time ver. 1.0.0"""
        json_data = swagger_hub_mock_v1_0_0.json()
        assert json_data["time"] == expected_time_in_json_payload
        assert json_data["seconds"] == expected_seconds_in_json_payload
        assert json_data["hours"]["top"] == expected_hours_top_in_json_payload
        assert json_data["hours"]["bottom"] == expected_hours_bottom_in_json_payload
        assert json_data["minutes"]["top"] == expected_minutes_top_in_json_payload
        assert json_data["minutes"]["bottom"] == expected_minutes_bottom_in_json_payload

    def should_find_the_same_reply_as_for_the_berlin_clock_get_time_v_1_0_0_contract():
        """🔌🎭 should find the function behind the API endpoint returns the right JSON schema as per the dictionary definition above"""
        response_berlin_clock_api = berlin_clock.berlin_clock_api(timestamp)
        assert response_berlin_clock_api.get("time") == expected_time_in_json_payload
        assert response_berlin_clock_api.get("seconds") == expected_seconds_in_json_payload
        assert response_berlin_clock_api.get("hours").get("top") == expected_hours_top_in_json_payload
        assert response_berlin_clock_api.get("hours").get("bottom") == expected_hours_bottom_in_json_payload
        assert response_berlin_clock_api.get("minutes").get("top") == expected_minutes_top_in_json_payload
        assert response_berlin_clock_api.get("minutes").get("bottom") == expected_minutes_bottom_in_json_payload


def describe_integration_test_to_ensure_the_api_exposed_on_localhost_is_the_same_as_in_the_contract_above():
    """📂 integration test to ensure the API exposed via FastAPI on localhost is the same as in the OPEN API specs"""

    def should_call_the_api_on_localhost_as_for_the_contract_ver_1_0_0(capsys):
        """🔌 should the FastAPI server running on localhost returns 200 and the proper json payload for 12:12:12"""
        stdout, stderr, returncode, params = start_api_on_unused_port_in_a_shell_and_stop_it_after_the_request(
            "12:12:12"
        )

        expected_json_payload = '{"time":"12:12:12","seconds":"Y","hours":{"top":"RROO","bottom":"RROO"},"minutes":{"top":"YYOOOOOOOOO","bottom":"YYOO"}}'
        assert returncode == 0
        assert "start_berlinclock_api_server_and_kill_it_after_the_test_call.sh" in params
        assert "200 OK" in stdout
        assert expected_json_payload in stdout
        assert "Shutting down" in stderr
        assert "Finished server process" in stderr

    def should_get_a_400_and_an_error_message_for_wrong_time():
        """🔌 should the FastAPI server running on localhost returns a 400 and an error message for the wrong timestamp"""
        stdout, stderr, returncode, params = start_api_on_unused_port_in_a_shell_and_stop_it_after_the_request(
            "99:99:99"
        )

        assert returncode == 0
        assert "start_berlinclock_api_server_and_kill_it_after_the_test_call.sh" in params
        assert "400 Bad Request" in stdout
        assert '{"detail":"Invalid time format. Please provide the time in 24HH:MM:ss' in stdout
        assert "Shutting down" in stderr
        assert "Finished server process" in stderr


# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
### UTILITY to set up the integration tests


def find_unused_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


def start_api_on_unused_port_in_a_shell_and_stop_it_after_the_request(timestamp):
    berlin_clock_ci_api_server_port = find_unused_port()
    command_to_run = f"./tests/integration/start_berlinclock_api_server_and_kill_it_after_the_test_call.sh {berlin_clock_ci_api_server_port} {timestamp}"

    command_executed = subprocess.run(
        command_to_run,
        capture_output=True,
        text=True,
        shell=True,
        check=True,
        timeout=10,
    )
    stdout = command_executed.stdout
    stderr = command_executed.stderr
    returncode = command_executed.returncode
    params = command_executed.args

    return stdout, stderr, returncode, params
