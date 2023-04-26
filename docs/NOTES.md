# Pomodoro Technique - Notes from the journey 🍅 by 🍅

## Pomodoro 1 🍅

Goal: Complete the kata as much as possible, starting from create the clock composition

- create the clock composition
  - clock composition string with everything is OFF --> midnight + 1sec => 00:00:01
- second component

## Pomodoro 2 🍅

- implement hours
- clock composition for hours

## Pomodoro 3 🍅

Goal: creating the hour module with integration of the bottom and top row of the hour

- ✅  Test with 5 AM
- 🚧  Test with 8 PM

- We should be agnostic of structure of the clock (bulbs, rows). Is it important to highlight the bulb or row?

## Pomodoro 4 🍅

Goal: creating the hour module with integration of the bottom and top row of the hour

- ✅  Test with 20:00:00 lights
- ✅  Test with 06:00:01 lights

## Pomodoro 5 🍅

Goal: minutes rows closing the end2end test
- ✅  Test minutes bottom row with 00:01:01
- ✅  Test minutes bottom row with 00:04:01
- ✅  Test minutes bottom row with 00:05:01
- ✅  Test minutes top row with 00:05:01 
- ✅  Test minutes top row with 00:10:01
- ✅  Test minutes top row with 00:15:01
- ✅  Test minutes top row with 00:30:01
- 🚧  Test minutes top row with 00:59:01
