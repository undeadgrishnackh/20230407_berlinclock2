Feature: WorldTimeAPI integration
  The user is expecting the time to be displayed using the WorldTimeAPI integration:

  🎙️ Request == IN:
     http://worldtimeapi.org/api/timezone/Europe/Berlin

  📦 Response == OUT:
     {
        "abbreviation": "CEST",
        "client_ip": "188.95.151.252",
        "datetime": "2023-08-30T15:36:29.256032+02:00",
        "day_of_week": 3,
        "day_of_year": 242,
        "dst": true,
        "dst_from": "2023-03-26T01:00:00+00:00",
        "dst_offset": 3600,
        "dst_until": "2023-10-29T01:00:00+00:00",
        "raw_offset": 3600,
        "timezone": "Europe/Berlin",
        "unixtime": 1693402589,
        "utc_datetime": "2023-08-30T13:36:29.256032+00:00",
        "utc_offset": "+02:00",
        "week_number": 35
      }

  Scenario: I lost my watch ⌚, and it's dinner time
    Given an user asks for the Berlin Clock API
    When they look at the clock at 19:36:01
    But they are too lazy to say which time it is
    Then the API should integrate with the time from the WorldTimeAPI
    And the API shold know it's 19:36:01
    And say it's O RRRO RRRR YYRYYRYOOOO YOOO
