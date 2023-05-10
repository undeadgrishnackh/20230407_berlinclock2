from pytest_bdd import given, when, then, scenarios

from modules.api import berlin_clock

scenarios("../features/api_berlin_clock.feature")


@given("an user asks for the Berlin Clock API")
def give_an_user_asks_the_berlin_clock_api(mocker):
    mocker.resetall()


@when("they look at the clock at 13:36:01", target_fixture="api_clock")
def api_clock():
    return berlin_clock.api("13:36:01")


@then("the API should say it's O RROO RRRO YYRYYRYOOOO YOOO")
def step_impl(api_clock):
    payload = api_clock
    assert payload.get("seconds") == "O"
    assert payload.get("hours").get("top") == "RROO"
    assert payload.get("hours").get("bottom") == "RRrO"
    assert payload.get("minutes").get("top") == "YYRYYRYOOOO"
    assert payload.get("minutes").get("bottom") == "YOOO"
