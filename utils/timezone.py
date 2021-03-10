import datetime
import time

from django.utils import timezone
from dateutil import rrule


def mktime(date=None, ts=True):
    if not date:
        date = timezone.now()

    if not ts:
        return time.mktime(date.timetuple())  # 1533697871.0

    return int(time.mktime(date.timetuple()))  # 1533697871.0


def now():
    return timezone.now()


def mktime_timedelta(days=None, ts=True):
    '''
    返回时间差 时间戳
    :param days:
    :param ts:
    :return:
    '''
    strftime = timezone.datetime.strptime(timezone.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    return int(time.mktime((strftime - timezone.timedelta(days=days)).timetuple()))


def time_long(date):
    '''
    计算 距今 多少天
    :param date: 传入时间对象 [以往时间]
    :return: 返回 [以往时间 距今时间] 之差 天数
    '''
    day = timezone.datetime.strptime(timezone.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
    strftime = timezone.datetime.strptime(date.strftime('%Y-%m-%d'), '%Y-%m-%d')
    times = int(time.mktime(day.timetuple())) - int(time.mktime(strftime.timetuple()))
    day_num = times / (24 * 60 * 60)
    return abs(int(day_num))


def nineteen_sub_time_long(date):
    if time_long(date) >= 90:
        return 0
    elif time_long(date) == 0:
        return 89
    return 89 - time_long(date)


def second_minus(minus):
    '''
    计算儿童出生年月日 距今时长 [年, 月, 日]
    :param minus: 需计算的日期对象，datatime对象
    :return: [年, 月, 日]
    '''

    month_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def is_leap(year):
        if year % 400 == 0 or year % 40 == 0 or year % 4 == 0:
            return True
        else:
            return False

    first_year = timezone.now().today()
    y = first_year.year - minus.year
    m = first_year.month - minus.month
    d = first_year.day - minus.day

    if d < 0:
        if minus.month == 2:
            if is_leap(minus.year):
                month_days[2] = 29

        d += month_days[minus.month]
        m -= 1

    if m < 0:
        m += 12
        y -= 1

    if y == 0:
        if m == 0:
            return [0, 0, int(d)]
        else:
            return [0, int(m), int(d)]
    else:
        return [int(y), int(m), int(d)]


def time_months(date):
    '''
    计算 距今 多少个月
    :param date:
    :return:
    '''
    time = now()
    d1 = datetime.date(date.year, date.month, date.day)
    d2 = datetime.date(time.year, time.month, time.day)

    return int(rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()) - 1


def time_years(date):
    '''
        计算 距今 多少年
        :param date:
        :return:
        '''
    date = str(date)[:19]
    import time
    date = time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')) + 8 * 3600
    time = time.mktime(time.localtime())
    date = datetime.datetime.fromtimestamp(date)
    time = datetime.datetime.fromtimestamp(time)
    d1 = datetime.date(date.year, date.month, date.day)
    d2 = datetime.date(time.year, time.month, time.day)
    if d1.month == 2 and d1.day == 29:
        d1 = datetime.date(date.year, date.month, date.day - 1)

    return int(rrule.rrule(rrule.YEARLY, dtstart=d1, until=d2).count()) - 1


def time_long_str(date):
    '''
    计算 距今 多少天
    :param date: 传入字符串 ’2013-09-23T14:10:51.939794+08:00‘
    :return: int 天数
    '''
    time_now = time.time()
    date = date[:10]
    date_time = time.mktime(time.strptime(date, '%Y-%m-%d'))
    times = time_now - date_time
    days_long = int(times / (24 * 60 * 60))
    return days_long
