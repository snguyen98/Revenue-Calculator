from datetime import datetime, timedelta, date

""" Calculates the nth day of the Week/Month/Year.
    E.g. The 7th Feb 2019 is the:
         - 4th day of the week (Thursday)
         - 7th day of the month
         - 38th day of the year
    Params: The date as a datetime object, type - Week, Month, Year
    Returns: The nth day of the type
"""
def get_excess(day, type):
    if (type == "Week"):
        return day.weekday() + 1
    elif (type == "Month"):
        return int(day.strftime("%d"))
    elif (type == "Year"):
        return day.timetuple().tm_yday
    else:
        return 0

""" Calculates the Weekly/Monthly/Yearly revenues.
    Params: File - Basic.txt, Deluxe.txt, Total.txt, type - Week, Month, Year
    Returns: A dictionary of revenues where the keys are the date at the start
             of the week, month or year depending on the input.
"""
def calc_rev(filename, type):
    file = open(filename, "r").readlines()[1:]
    curr_day = datetime.today()
    rev = {}
    pos = len(file) - 1

    # Iterate backwards through the file starting from 'Today'.
    while (pos >= 0):
        sum = 0  # Resets for each week/month/year

        # Sum all values for the current week/month/year.
        for i in range(0, get_excess(curr_day, type)):
            if (pos < 0):
                break
            else:
                sum += int(file[pos])
                pos -= 1

        # Multiplies the sum by cost of each cupcake if basic or deluxe file.
        if (file == "Basic.txt"):
            sum *= 5  # Each basic cupcake costs $5
        elif (file == "Deluxe.txt"):
            sum *= 6  # Each deluxe cupcake costs $6

        # Generate the key names as dates in the form:
        # - dd/mm/yy for type Week
        # - mm/yy for type Month
        # - yy for type Year
        key = ""
        if (type == "Week"):
            end_week = curr_day + timedelta(6)
            key = curr_day.strftime("%d/%m/%Y") + " - "
                        + end_week.strftime("%d/%m/%Y")
        elif (type == "Month"):
            key = curr_day.strftime("%m/%Y")
        else:
            key = curr_day.strftime("%Y")

        # Adds the revenue to the dictionary.
        curr_day -= timedelta(get_excess(curr_day, type) - 1)
        rev[key] = sum
        curr_day -= timedelta(1)

    return rev
