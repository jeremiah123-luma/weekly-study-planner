# Test Table – Weekly Study Planner

Run with `python3 planner.py`. Daily limit = 6 hours.

| # | Type | Input | Expected result | Actual result |
|---|------|-------|-----------------|---------------|
| 1 | Typical | Sun 3, Mon 5, Tue 7, Wed 4, Thu 2, Fri 1, Sat 0 (with descriptions) | Total 22. Busiest Tuesday (7), lightest Saturday (0). Warning on Tuesday only. Tip: move 1 hour Tuesday → Saturday. | Matches expected. |
| 2 | Invalid | Monday: `abc`, then `-2`, then `4` | Each bad entry prints the error and asks again. Monday saved as 4. | Matches expected. |
| 3 | Invalid | Monday: `nan`, `inf`, `30`, then `2.5` | All three rejected (not real hours / over 24). Monday saved as 2.5. | Matches expected (found during testing, fixed by adding the 0–24 range check). |
| 4 | Unusual | 0 hours all week, all descriptions blank | Every day shows "No work". No warnings. Prints "No work entered this week." | Matches expected. |
| 5 | Edge (limit) | Sun 6, Mon 6, Tue 2, Wed 3, Thu 1, Fri 0, Sat 4 | Total 22. No warnings (6 = limit, not over). Busiest Sunday (first of the tie), lightest Friday. No tip. | Matches expected. |
