from datetime import datetime
import calendar

# ANSI escape codes for text color
CYAN = "\033[96m"
RESET = "\033[0m"

# Get the list of weekday names starting from Monday
weekdays_starting_from_monday = list(calendar.day_name)
weekend_days = weekdays_starting_from_monday[5:]

friends = [
	{"name": "Nadia Shostak", "birthday": datetime(1955, 5, 13)},
	{"name": "Maria Horeva", "birthday": datetime(1955, 8, 22)},
	{"name": "Myhailo Lohachov", "birthday": datetime(1955, 12, 1)},
	{"name": "Olha Myronenko", "birthday": datetime(1955, 12, 1)},
	{"name": "Artem Stepanenko", "birthday": datetime(1955, 11, 30)},
	{"name": "Nataliia Shevchenko", "birthday": datetime(1955, 9, 26)},
]

def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays_per_week = dict()

    for user in users:
        user_name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if delta_days > 7:
            continue

        day_name = birthday_this_year.strftime("%A")
        # ? need to check this condition
        if day_name in weekend_days:
            day_name = 'Monday'
        if not day_name in birthdays_per_week:
            birthdays_per_week[day_name] = []
        birthdays_per_week[day_name].append(user_name)

    for week_day in weekdays_starting_from_monday:
        if not week_day in birthdays_per_week:
            continue
        names = ', '.join(birthdays_per_week[week_day])
        print('{:<18}: {:<}'.format(CYAN + week_day + RESET, names))

get_birthdays_per_week(friends)
