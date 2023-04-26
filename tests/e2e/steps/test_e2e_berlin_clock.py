import sys

from pytest_bdd import given, when, then, scenarios

from modules.berlin_clock import berlin_clock

scenarios("../features/berlin_clock.feature")


@given("an user in front of the Berlin Clock")
def give_a_developer(mocker):
    mocker.resetall()


@when("they look at the clock at 12:56:01", target_fixture="clock")
def clock(capsys):
    display = berlin_clock("12:56:01")
    out, err = capsys.readouterr()
    return display, out.strip(), err.strip()


@then("light should be like O RROO RROO YYRYYRYYRYY YOOO")
def then_the_title_is_printed(clock):
    display, out, err = clock
    assert "O\nRROO\nRROO\nYYRYYRYYRYY\nYOOO" in display
    assert out == ""
    assert err == ""
