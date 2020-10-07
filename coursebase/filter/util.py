import datetime


def get_time_index():
    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    if (h > 8 and h < 21) or (h == 8 and m >= 30):
        return (h - 9) + 1 if m >= 30 else 0
    return 0


def get_day_index():
    return datetime.datetime.now().weekday() + 1
