from datetime import datetime, timedelta, date

def get_excess(day, type):
    if (type == "Week"):
        return day.weekday() + 1
    elif (type == "Month"):
        return int(day.strftime("%d"))
    elif (type == "Year"):
        return day.timetuple().tm_yday
    else:
        return 0

def calc_rev(filename, type):
    file = open(filename, "r").readlines()[1:]
    curr_day = datetime.today()
    rev = {}
    pos = len(file) - 1
    while (pos >= 0):
        sum = 0
        for i in range(0, get_excess(curr_day, type)):
            if (pos < 0):
                break
            else:
                sum += int(file[pos])
                pos -= 1
        if (file == "Basic.txt"):
            sum *= 5
        elif (file == "Basic.txt"):
            sum *= 6
        key = ""
        if (type == "Week"):
            end_week = curr_day + timedelta(6)
            key = curr_day.strftime("%d/%m/%Y") + " - " + end_week.strftime("%d/%m/%Y")
        elif (type == "Month"):
            key = curr_day.strftime("%m/%Y")
        else:
            key = curr_day.strftime("%Y")
        curr_day -= timedelta(get_excess(curr_day, type) - 1)
        rev[key] = sum
        curr_day -= timedelta(1)

    return rev
