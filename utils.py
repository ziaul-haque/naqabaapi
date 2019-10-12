from datetime import datetime, date
from pytz import timezone as tz

local_time_zone = 'Asia/Riyadh'


def convert_datetime_to_timezone(dt):
    try:
        # if naive object first converts a naive datetime object into a
        # timezone-aware datetime object.
        dt = tz("UTC").localize(dt)
    except ValueError:
        # raise when not naive datetime
        pass
    return dt.astimezone(tz(local_time_zone))


def get_current_datetime():
    """
    Return current date instance of datetime.date
    """
    now_utc = datetime.now(tz('UTC'))
    return convert_datetime_to_timezone(now_utc)


def get_current_date_obj():
    """
    Return current date instance of datetime.date
    """
    return get_current_datetime().date()


def get_current_date_str():
    """
    Return current date in string (i.e YYYY-MM-DD format)
    """
    return get_current_date_obj().strftime('%Y-%m-%d')


def get_datetime_obj_from_str(datetime_str, _format='%Y-%m-%d'):
    try:
        return datetime.strptime(datetime_str, _format)
    except ValueError:
        raise ValueError("Incorrect date format of %s" % datetime_str)


def get_diff_day(d1, d2):
    delta = d1 - d2
    return delta.days


