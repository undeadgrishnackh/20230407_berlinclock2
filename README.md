![Build Status](https://github.com/undeadgrishnackh/20230407_berlinclock2/actions/workflows/cicd.yml/badge.svg)
[![CodeScene general](https://codescene.io/images/analyzed-by-codescene-badge.svg)](https://codescene.io/projects/39650)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=undeadgrishnackh_20230407_berlinclock2&metric=coverage)](https://sonarcloud.io/summary/new_code?id=undeadgrishnackh_20230407_berlinclock2)

                

# BerlinClock Kata   

## The Kata

The kata is from [CodeWars](https://www.codewars.com/kata/5a1463678ba9145a670000f9).

## Handicap rules

- Double loop (BDD - TDD) : E2E tests defined in gherkin 🥒 and then iterate in the internal loop via atomic ⚛️ unit tests.
- CI/CD pipeline with GitHub Actions
- local quality gate with linter, black, conventional commits, etc.
- HEX Architecture

## 🎯Target

- BerlinClock Domain wrapped into an API server
- API dictionary defined via OpenAPI
- API Server tested with:
  - contract test
  - integration tests during the CI
  - smoke test post delivery
- Api Server packaged into a container
- Container build and tested to ensure: linter, structure, security, efficiency 

---

## Description of the kata

The "Berlin Clock" is the first public clock in the world that tells the time by means of illuminated, coloured fields, for which it entered the Guinness Book of Records upon its installation on 17 June 1975.

![Berlin clock](./docs/img/img.png)

The clock is read from the top row to the bottom. The top row of four red fields denote five full hours each, alongside the second row, also of four red fields, which denote one full hour each, displaying the hour value in 24-hour format. The third row consists of eleven yellow-and-red fields, which denote five full minutes each (the red ones also denoting 15, 30 and 45 minutes past), and the bottom row has another four yellow fields, which mark one full minute each. The round yellow light on top blinks to denote even- (when lit) or odd-numbered (when unlit) seconds.

Example: Two fields are lit in the first row (five hours multiplied by two, i.e. ten hours), but no fields are lit in the second row; therefore the hour value is 10.
Six fields are lit in the third row (five minutes multiplied by six, i.e. thirty minutes), while the bottom row has one field on (plus one minute). Hence, the lights of the clock altogether tell the time as 10:31. (Source: Wikipedia)

Task: Write a function that takes in a particular time as 24h format ('hh:mm:ss') and outputs a string that reproduces the Berlin Clock. The parameters should be as follows:

“O” = Light off
“R” = Red light
“Y” = Yellow light

Example Test Case:
Input String:
12:56:01

Output String:
O
RROO
RROO
YYRYYRYYRYY
YOOO