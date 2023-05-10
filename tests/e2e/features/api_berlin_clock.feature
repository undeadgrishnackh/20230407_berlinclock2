Feature: Berlin Clock as an API
  use the Berlin Clock login as an API

  Scenario: 🕛 it's italian lunch time!
    Given an user asks for the Berlin Clock API
    When they look at the clock at 13:36:01
    Then the API should say it's O RROO RRRO YYRYYRYOOOO YOOO
