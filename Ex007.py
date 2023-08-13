import logging
import argparse

logging.basicConfig(
    filename='test.log',
    encoding='utf-8',
    format='{levelname} {funcName} -> {msg}',
    style='{',
    level=logging.ERROR
)


def leap_year(year):
    logger = logging.getLogger('main')
    try:
        year = int(year)
    except:
        logger.error(f'Неверный формат года - > {year}')
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result


def simple_gen(num):
    logger = logging.getLogger('main')
    try:
        num = int(num)
    except:
        logger.error(f'Неверный формат числа - > {num}')
    res = []
    i = 1
    data = 1
    while num != 0:
        check = 0
        while i <= data:
            if data % i == 0:
                check += 1
            i += 1
        if check == 2:
            res.append(data)
            num -= 1
        i = 1
        data += 1
    return res


if __name__ == '__main__':
    """
    python Homework15\Ex007.py -num '5' -year '2000'
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-num', type=str)
    parser.add_argument('-year', type=str)
    args = parser.parse_args()
    print(leap_year(args.year))
    print(simple_gen(args.num))