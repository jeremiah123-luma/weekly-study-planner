# Test Table – Weekly Study Planner

Run with `python3 planner.py`. Daily limit = 6 hours.

| # | Type | Input | Expected result | Actual result |
|---|------|-------|-----------------|---------------|
| 1 | Typical | Sun 3, Mon 5, Tue 7, Wed 4, Thu 2, Fri 1, Sat 0 (with descriptions) | Total 22. Busiest Tuesday (7), lightest Saturday (0). Warning on Tuesday only. Tip: move 1 hour Tuesday → Saturday. | Total 22. Busiest Tuesday (7 hrs), lightest Saturday (0 hrs). Warning on Tuesday only. "Tip: try moving 1 hour(s) from Tuesday to Saturday." |
| 2 | Invalid | Monday: `abc`, then `-2`, then `4` | Each bad entry prints the error and asks again. Monday saved as 4. | "Please enter a number from 0 to 24." printed twice, then Monday saved as 4 hrs. |
| 3 | Invalid | Monday: `30`, blank, `nan`, `1e5`, then `4` | All rejected (over 24, empty, not plain numbers). Monday saved as 4. | Error printed 4 times, Monday saved as 4 hrs. No crash. |
| 4 | Unusual (decimals) | Sun `2.5`, Mon `.5`, Tue `5.`, Wed `24`, rest 0 | Decimals accepted. 24 is allowed but over the limit. Tip limited to what Thursday can hold. | Sun 2.5, Mon 0.5, Tue 5, Wed 24 with warning. Total 32. "Tip: try moving 6 hour(s) from Wednesday to Thursday." |
| 5 | Unusual (empty week) | 0 hours all week, all descriptions blank | Every day shows "No work". No warnings. "No work entered this week." | Matches expected exactly. |
| 6 | Unusual (all equal) | 8 hours every day | Warning on all 7 days. No busiest/lightest (all the same). No day has room, so no "move" tip. | "Every day has the same workload (8 hrs)." then "Tip: every day is at or over the limit. Try cutting or pushing back some work." |
| 7 | Edge (limit) | Sun 6, Mon 6, Tue 2, Wed 3, Thu 1, Fri 0, Sat 4 | Total 22. No warnings (6 = limit, not over). Busiest Sunday (first of the tie), lightest Friday. No tip. | Matches expected exactly. |

**Bugs found while testing (and fixed):**
- Our first version accepted `nan` and `inf` as hours, because Python's `float()` treats them as numbers. Fixed by checking the characters with string methods (Module 7) before converting.
- When every day had the same hours, it printed "Busiest: Sunday, Lightest: Sunday" and suggested moving hours from Sunday to Sunday. Fixed by checking for that case first.
- The tip could push the lightest day over the limit too (e.g., moving 6 hours onto a 5-hour day). Fixed by only suggesting as much as the lightest day can hold.
