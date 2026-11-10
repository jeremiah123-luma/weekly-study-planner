# Weekly Study Planner

CS 100 Roadmap Project · Team 20 · Jeremiah, Robert, Elijah

A Python program that walks you through the week (Sunday → Saturday), asks how many hours of work you have each day and what it is, then prints a plan: weekly total, busiest and lightest days, a warning on any day over 6 hours, and a tip for moving hours off the busiest day.

## Run it

```
python3 planner.py
```

## Files

- `planner.py` – the program (7 functions from our Milestone 2 design, plus `is_valid_hours` and `format_hours` helpers)
- `TESTS.md` – test table (typical, invalid, unusual, edge) with actual output
- `AI_USE.md` – AI Use Statement (draft)
- `MILESTONE3_UPDATE.md` – draft of our progress update (due Nov 16)

## Course concepts used (all from Modules 2–8)

- **Lists**: `DAYS`, `hours`, `descriptions`
- **for loops**: go through the days to ask questions and print the plan, and go through each character of an answer to check it
- **while loop**: keeps asking until the hours entered are valid
- **Decisions (if/elif/else)**: input checks, overload warnings, empty-week and same-hours messages
- **Functions**: 9 total, each with a docstring
- **Strings**: joining text with `+`, checking characters with `in`
- **Built-ins**: `input`, `print`, `len`, `range`, `min`, `int`, `float`, `str`, list `append`

## Still to do (Milestone 4, due Nov 30)

- [ ] Each of us reads through every function and can explain it
- [ ] Rewrite the comments in our own words (rubric requirement)
- [ ] Optional extras from the proposal: user sets their own daily limit, text bar chart
- [ ] Team reflection (500–700 words) + individual notes
- [ ] AI Use Statement
