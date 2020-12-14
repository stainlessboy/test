import datetime
import math


def delta_time(date=None, days=0) -> datetime:
    if not date:
        date = datetime.datetime.today()
    date = date + datetime.timedelta(days=days)
    return date
