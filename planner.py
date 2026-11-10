# Weekly Study Planner
# CS 100 Roadmap Project, Team 20 (Jeremiah, Robert, Elijah)
#
# What it does: walks the user through the week, Sunday to Saturday,
# asks how many hours of work they have each day and what the work is,
# then prints a plan with the weekly total, the busiest and lightest
# days, a warning for any day over the daily limit, and a tip for
# moving hours from the busiest day to the lightest one.

# The seven days, in the order the program asks about them.
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Most hours we think is reasonable for one day. Kept in one spot so
# it is easy to change.
DAILY_LIMIT = 6


def get_daily_hours(day):
    """Ask how many hours of work the user has on `day`.
    Keeps asking until the answer is a number 0 or higher, then returns it."""
    while True:
        answer = input(f"How many hours of work do you have on {day}? ").strip()
        # float() crashes on text like "abc", so try/except catches that
        # and lets us ask again instead of the program stopping.
        try:
            hours = float(answer)
        except ValueError:
            print("Please enter a number from 0 to 24.")
            continue
        # A number came in, but it has to fit in a real day.
        # Writing it as "0 <= hours <= 24" also rejects tricky inputs like
        # "inf" and "nan", which float() accepts but aren't real hours.
        if 0 <= hours <= 24:
            return hours
        print("Please enter a number from 0 to 24.")


def get_description(day):
    """Ask for a short description of the day's work.
    Returns "No work" if the user leaves it blank."""
    description = input(f"What is the work on {day}? (press Enter to skip) ").strip()
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
        line = f"{days[i]:<10} {format_hours(hours[i]):>5} hrs  {descriptions[i]}"
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
    print(f"Weekly total: {format_hours(total)} hours")
    print(f"Busiest day:  {busiest} ({format_hours(busiest_hours)} hrs)")
    print(f"Lightest day: {lightest} ({format_hours(hours[days.index(lightest)])} hrs)")

    if check_overload(busiest_hours, limit):
        extra = busiest_hours - limit
        print(f"Tip: try moving {format_hours(extra)} hour(s) from {busiest} to {lightest}.")


def main():
    """Run the program: collect each day's input, then print the plan."""
    print("Welcome to the Weekly Study Planner!")
    print(f"Daily limit is set to {DAILY_LIMIT} hours.\n")
    hours = []
    descriptions = []
    for day in DAYS:
        hours.append(get_daily_hours(day))
        descriptions.append(get_description(day))
    print_plan(DAYS, hours, descriptions, DAILY_LIMIT)


# Only run main() when this file is run directly (not when tests import it).
if __name__ == "__main__":
    main()
