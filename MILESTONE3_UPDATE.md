# Milestone 3: Progress Discussion – Team 20 (Weekly Study Planner)

**What currently works:** All three core features run. The program asks for hours and a description for each day, Sunday through Saturday, and keeps re-asking until it gets a number from 0 to 24. It then prints one line per day, flags any day over the 6-hour limit, shows the weekly total and the busiest and lightest days, and suggests how many hours to move. All four test cases from our design (typical, invalid, all zeros, and a day exactly at the limit) give the results we expected, along with three extra cases we added.

**What remains:** Each of us still needs to go through the code until we can explain every function, and rewrite the comments in our own words. If time allows, we want to add the two extras from our proposal: letting the user set their own daily limit, and a text bar chart of hours per day. We also have the reflection and the AI Use Statement left to write.

**One challenge or scope concern:** Testing showed our first input check let "nan" and "inf" through, because Python's `float()` counts them as numbers. We fixed it by looping through each character to make sure it's only digits and one decimal point, and by limiting entries to 0–24 hours. Testing also showed odd output when every day had the same hours, which we fixed. Our main concern now is making sure all three of us understand the code equally.

**How AI was used:** We used Claude to help write the Python code from our Milestone 2 pseudocode and function breakdown, and to run our test cases. The design (features, functions, and tests) was ours from Milestones 1 and 2. Since AI helped with the code, we're reviewing it line by line so each of us can explain it, and we'll describe that in the reflection.
