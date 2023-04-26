# TechDebt that is emerging

More the code, more are the debts. Keep here which kind of debts were being made due to your choices.

# TODO: TECHDEBT: timestamp in every modules is a waste of CPU, chop it at the beginning

[ ] No Guardian test
[ ] test boundaries(of component functions i.e. "00:00:60", "24:00:00", or "0:99:00", or "00:100:00", "aa:00:00)
✅ parse the input of the timestamp once.
🚧 Convert return of split_timestamp to tuple to improve readability
🚧 Consistent name 
✅ Return of timestamp split is not readable as it should be.
✅Remove duplication of code for timestamp splitting
[ ] test boundaries("1:00:00", "24:00:00")
[ ] test 01:00:01 => better to use different values (eg. "01:02:03")
✅ Rewrite tests to ensure same domain language
[ ] Rename method seconds_bulb for consistency with other component methods
[ ] Improve Groovy Script to change to SnakeCase
[ ] Refactor tests as table-driven tests to avoid repetition/lots of typing
