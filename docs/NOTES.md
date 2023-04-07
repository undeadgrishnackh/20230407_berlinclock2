# Pomodoro Technique - Notes from the journey 🍅 by 🍅

## Pomodoro 1 🍅

Goal: Complete the kata as much as possible, starting from create the clock compositiokn

- create the clock composition
  - clock composition string with everything is OFF --> midnight + 1sec => 00:00:01
- second component

## TECHDEBT:

🚧 test boundaries(i.e. "00:00:60", "24:00:00", or "0:99:00", or "00:100:00", "aa:00:00)
✅ parse the input of the timestamp once.
🚧 Convert return of split_timestamp to tuple to improve readability
🚧 Consistent name of component functions.


## Pomodoro 2 🍅

- implement hours
- clock composition for hours
- 
🚧 TECHDEBT:
[ ] test boundaries("1:00:00", "24:00:00")
[ ] test 01:00:01 => better to use different values (eg. "01:02:03")
