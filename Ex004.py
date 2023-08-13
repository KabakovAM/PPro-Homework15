from datetime import date
import logging

logging.basicConfig(
    filename='data.log',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.ERROR
)

def from_str_to_data(data: str):
    day_dict = {'по': 1, 'вт': 2, 'ср': 3, 'че': 4, 'пя': 5, 'су': 6, 'во': 7}
    month_dict = {'ян': 1, 'фе': 2, 'ма': 3, 'ап': 4, 'ма': 5, 'ию': [6, 7], 'ав': 8, 'се': 9, 'ок': 10, 'но': 11, 'де': 12}
    data_list = data.split()
    try:   
        num = int(data_list[0][0])
        day_week = day_dict[data_list[1][:2]] - 1
        month = month_dict[data_list[2][:2]]
        if month == [6, 7] and data_list[2][:3] == 'июн':
            month = 6
        elif month == [6, 7] and data_list[2][:3] == 'июл':
            month = 7
    except:
        logger = logging.getLogger('main')
        logger.error('Неверный формат ввода данных!')        
    year = date.today().year
    count = 1
    for day in range(1,31):
        result = date(year=year, month=month, day=day)
        if result.weekday() == day_week:
            if count == num:
                return result
            else:
                count+=1

if __name__ == '__main__':
    data = '1-й четверг июля'
    print(from_str_to_data(data))