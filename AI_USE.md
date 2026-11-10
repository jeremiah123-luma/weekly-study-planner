# AI Use Statement – Team 20

> DRAFT. The team should check this is accurate and edit it before submitting.

**Tool:** Claude (Anthropic).

**What it helped with:**
- Milestone 2: helped us understand how the program should flow, and reviewed our pseudocode. It caught that we were missing the weekly total and the overload check.
- Milestone 3/4: wrote the first version of the Python code from our Milestone 2 pseudocode and function breakdown, and ran our test cases.

**What stayed ours:** the problem, the three core features, the function list, the daily limit, and the test cases all came from our Milestone 1 proposal and Milestone 2 design.

**How we checked and revised it:**
- Ran every test case in `TESTS.md` and compared the output to what our design said should happen.
- Testing turned up three bugs (`nan`/`inf` accepted, "busiest Sunday / lightest Sunday" when all days are equal, and a tip that could overload the lightest day), which were fixed.
- Had all code outside our course (`try/except`, f-strings, string methods we weren't sure were covered) replaced with loops, if/else, and lists from Modules 2–8.
- [TEAM: describe your own review here, e.g., each member went through the code line by line and rewrote the comments in their own words.]
