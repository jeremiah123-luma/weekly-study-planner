# Weekly Study Planner
# CS 100 Roadmap Project, Team 20 (Jeremiah, Robert, Elijah)
#
# What it does: walks the user through the week, Sunday to Saturday,
# asks how many hours of work they have each day and what the work is,
# then prints a plan with the weekly total, the busiest and lightest
# days, a warning for any day over the daily limit, and a tip for
# moving hours from the busiest day to the lightest one.
#
# AI Use Statement: see AI_USE.md in this folder.

# The seven days, in the order the program asks about them (a list).
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Most hours we think is reasonable for one day. Kept in one spot so
# it is easy to change.
DAILY_LIMIT = 6


def is_valid_hours(answer):
    """Return True if `answer` is a number from 0 to 24, like "4" or "2.5".
    Anything else (letters, a minus sign, blank) returns False."""
    # Take out ONE decimal point, then every character left must be a digit.
    # "2.5" -> "25" (ok), "-2" -> "-2" (has a minus, not ok), "abc" (not ok).
    without_point = answer.replace(".", "", 1)
    if not without_point.isdecimal():
        return False
    # It's a number now, so it's safe to turn it into a float.
    # A day only has 24 hours, so anything bigger is a typo.
    return float(answer) <= 24


def get_daily_hours(day):
    """Ask how many hours of work the user has on `day`.
    Keeps asking until the answer is valid, then returns it as a float."""
    answer = input("How many hours of work do you have on " + day + "? ").strip()
    while not is_valid_hours(answer):
        print("Please enter a number from 0 to 24.")
        answer = input("How many hours of work do you have on " + day + "? ").strip()
    return float(answer)


def get_description(day):
    """Ask for a short description of the day's work.
    Returns "No work" if the user leaves it blank."""
    description = input("What is the work on " + day + "? (press Enter to skip) ").strip()
    if description == "":
        return "No work"
    return description


def calculate_total(hours):
    """Add up the list of hours and return the weekly total."""
    total = 0
    for h in hours:
        total = total + h
    return total


def find_busiest_and_lightest(days, hours):
    """Return the day with the most hours and the day with the fewest.
    If two days tie, the earlier one in the week wins."""
    busiest_index = 0
    lightest_index = 0
    for i in range(1, len(hours)):
        # Strict > and < mean a tie keeps the earlier day.
        if hours[i] > hours[busiest_index]:
            busiest_index = i
        if hours[i] < hours[lightest_index]:
            lightest_index = i
    return days[busiest_index], days[lightest_index]


def check_overload(day_hours, limit):
    """Return True if a day's hours go OVER the limit (equal is fine)."""
    return day_hours > limit


def format_hours(h):
    """Show 4.0 as "4" but keep 2.5 as "2.5" so the output looks clean."""
    if h == int(h):
        return str(int(h))
    return str(h)


def print_plan(days, hours, descriptions, limit):
    """Print one line per day (with warnings), then the weekly summary."""
    print()
    print("===== Your Weekly Plan =====")
    for i in range(len(days)):
        # ljust/rjust pad the text with spaces so the columns line up.
        line = days[i].ljust(10) + format_hours(hours[i]).rjust(5) + " hrs  " + descriptions[i]
        if check_overload(hours[i], limit):
            line = line + "   <-- Warning: over the limit"
        print(line)
    print("============================")

    total = calculate_total(hours)
    if total == 0:
        print("No work entered this week.")
        return

    busiest, lightest = find_busiest_and_lightest(days, hours)
    # .index() finds where a day sits in the list so we can grab its hours.
    busiest_hours = hours[days.index(busiest)]
    lightest_hours = hours[days.index(lightest)]
    print("Weekly total: " + format_hours(total) + " hours")
    if busiest_hours == lightest_hours:
        # Every day is the same, so "busiest Sunday, lightest Sunday" would look odd.
        print("Every day has the same workload (" + format_hours(busiest_hours) + " hrs).")
    else:
        print("Busiest day:  " + busiest + " (" + format_hours(busiest_hours) + " hrs)")
        print("Lightest day: " + lightest + " (" + format_hours(lightest_hours) + " hrs)")

    if check_overload(busiest_hours, limit):
        extra = busiest_hours - limit      # hours the busiest day is over by
        room = limit - lightest_hours      # hours the lightest day can still take
        if room <= 0:
            # Every day is already at or over the limit, so there's nowhere to move work.
            print("Tip: every day is at or over the limit. Try cutting or pushing back some work.")
        else:
            # Only suggest moving as much as the lightest day can hold,
            # so the tip never pushes that day over the limit too.
            move = min(extra, room)
            print("Tip: try moving " + format_hours(move) + " hour(s) from " + busiest + " to " + lightest + ".")


def main():
    """Run the program: collect each day's input, then print the plan."""
    print("Welcome to the Weekly Study Planner!")
    print("Daily limit is set to " + str(DAILY_LIMIT) + " hours.")
    print()
    hours = []
    descriptions = []
    for day in DAYS:
        hours.append(get_daily_hours(day))
        descriptions.append(get_description(day))
    print_plan(DAYS, hours, descriptions, DAILY_LIMIT)


main()
