Feature: Berlin Clock
  A strange light bulbs clock situated in Germany (Berlin) that tells you the time
  with a weird light algorithm based on the number of seconds, minutes and hours
  that have passed since midnight displayed in a 5x5 grid of light bulbs.

  Scenario: 🕛 it's lunch time!
    Given an user in front of the Berlin Clock
    When they look at the clock at 12:56:01
    Then light should be like O RROO RROO YYRYYRYYRYY YOOO
    #            ⚫️
    #    🔴   🔴   ⚫ ️  ⚫️
    #    🔴   🔴   ⚫ ️  ⚫️
    #    🟡🟡🔴🟡🟡🔴🟡🟡🔴🟡🟡
    #    🟡   ⚫️   ⚫️    ⚫️