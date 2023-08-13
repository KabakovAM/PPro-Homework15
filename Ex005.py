from datetime import date
import logging
import argparse


logging.basicConfig(
    filename='data.log',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.ERROR
)


def from_str_to_data(num, day_week, month):
    day_dict = {'по': 0, 'вт': 1, 'ср': 2, 'че': 3, 'пя': 4, 'су': 5, 'во': 6}
    month_dict = {'ян': 1, 'фе': 2, 'ма': 3, 'ап': 4, 'ма': 5, 'ию': [6, 7], 'ав': 8, 'се': 9, 'ок': 10, 'но': 11, 'де': 12}
    try:
        num = int(num[0])
        if not (day_week in list(day_dict.values())):
            day_week = day_dict[day_week[:2]]
        temp = month_dict[month[:2]]
        if temp == [6, 7] and month[:3] == 'июн':
            month = 6
        elif temp == [6, 7] and month[:3] == 'июл':
            month = 7
        else:
            month = temp
    except:
        logger = logging.getLogger('main')
        logger.error('Неверный формат ввода данных!')
    year = date.today().year
    count = 1
    for day in range(1, 31):
        result = date(year=year, month=month, day=day)
        if result.weekday() == day_week:
            if count == num:
                return result
            else:
                count += 1


if __name__ == '__main__':
    """
    python Homework15\Ex005.py -num '1-й' -day_week 'понедельник' -month 'июля'
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-num', type=str, default='1-й')
    parser.add_argument('-day_week', type=str, default=date.today().weekday())
    parser.add_argument('-month', type=str, default=date.today().month)
    args = parser.parse_args()
    print(from_str_to_data(args.num, args.day_week, args.month))

