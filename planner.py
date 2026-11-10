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
    '''Return True if answer is a number from 0 to 24, like "4" or "2.5".
    Anything else (letters, a minus sign, spaces, blank) returns False.'''
    # A blank answer or a lone "." isn't a number.
    if answer == "" or answer == ".":
        return False
    # Look at every character: only digits and a decimal point are allowed.
    # This is what rejects "abc", "-2", "nan", and "1e5".
    dots = 0
    for ch in answer:
        if ch == ".":
            dots = dots + 1
        elif ch not in "0123456789":
            return False
    # "2.5" is fine, but "2.5.1" (two decimal points) is not.
    if dots > 1:
        return False
    # Now it's safe to turn it into a number. A day only has 24 hours.
    return float(answer) <= 24


def get_daily_hours(day):
    '''Ask how many hours of work the user has on day.
    Keeps asking until the answer is valid, then returns it as a number.'''
    answer = input("How many hours of work do you have on " + day + "? ")
    while not is_valid_hours(answer):
        print("Please enter a number from 0 to 24.")
        answer = input("How many hours of work do you have on " + day + "? ")
    return float(answer)


def get_description(day):
    '''Ask for a short description of the day's work.
    Returns "No work" if the user leaves it blank.'''
    description = input("What is the work on " + day + "? (press Enter to skip) ")
    if description == "":
        return "No work"
    return description


def calculate_total(hours):
    '''Add up the list of hours and return the weekly total.'''
    total = 0
    for h in hours:
        total = total + h
    return total


def find_busiest_and_lightest(hours):
    '''Return a list of two positions: [busiest day, lightest day].
    If two days tie, the earlier one in the week wins.'''
    busiest = 0
    lightest = 0
    for i in range(1, len(hours)):
        # Strict > and < mean a tie keeps the earlier day.
        if hours[i] > hours[busiest]:
            busiest = i
        if hours[i] < hours[lightest]:
            lightest = i
    return [busiest, lightest]


def check_overload(day_hours, limit):
    '''Return True if a day's hours go OVER the limit (equal is fine).'''
    return day_hours > limit


def format_hours(h):
    '''Show 4.0 as "4" but keep 2.5 as "2.5" so the output looks clean.'''
    if h == int(h):
        return str(int(h))
    return str(h)


def print_plan(days, hours, descriptions, limit):
    '''Print one line per day (with warnings), then the weekly summary.'''
    print()
    print("===== Your Weekly Plan =====")
    for i in range(len(days)):
        line = days[i] + ": " + format_hours(hours[i]) + " hrs - " + descriptions[i]
        if check_overload(hours[i], limit):
            line = line + "   <-- Warning: over the limit"
        print(line)
    print("============================")

    total = calculate_total(hours)
    if total == 0:
        print("No work entered this week.")
    else:
        positions = find_busiest_and_lightest(hours)
        busiest = positions[0]       # position of the busiest day in the lists
        lightest = positions[1]      # position of the lightest day in the lists
        print("Weekly total: " + format_hours(total) + " hours")

        if hours[busiest] == hours[lightest]:
            # Every day is the same, so "busiest Sunday, lightest Sunday" would look odd.
            print("Every day has the same workload (" + format_hours(hours[busiest]) + " hrs).")
        else:
            print("Busiest day: " + days[busiest] + " (" + format_hours(hours[busiest]) + " hrs)")
            print("Lightest day: " + days[lightest] + " (" + format_hours(hours[lightest]) + " hrs)")

        if check_overload(hours[busiest], limit):
            extra = hours[busiest] - limit     # hours the busiest day is over by
            room = limit - hours[lightest]     # hours the lightest day can still take
            if room <= 0:
                # Every day is at or over the limit, so there's nowhere to move work.
                print("Tip: every day is at or over the limit. Try cutting or pushing back some work.")
            else:
                # Only suggest moving as much as the lightest day can hold,
                # so the tip never pushes that day over the limit too.
                move = min(extra, room)
                print("Tip: try moving " + format_hours(move) + " hour(s) from "
                      + days[busiest] + " to " + days[lightest] + ".")


def main():
    '''Run the program: collect each day's input, then print the plan.'''
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
