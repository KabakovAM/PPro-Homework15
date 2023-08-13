import logging

logging.basicConfig(
    filename='guess.log',
    encoding='utf-8',
    format='{levelname} {asctime} {msg}',
    style='{',
    level=logging.INFO
)

def save_func_to_log(func):
    def wraper(*args, **kwargs):
        logger = logging.getLogger('main')
        result = func(*args, **kwargs)
        logger.info({'funcName' : func.__name__, 'args' : args, 'kwargs': kwargs, 'result': result})
    return wraper


@save_func_to_log
def guess(answer, attempts):
    for _ in range(attempts):
        data = int(input('Введите число: '))
        if data == answer:
            print('Число угадано!')
            return True
        elif data < answer:
            print('Больше!')
        else:
            print('Меньше!')
    print('Вы проиграли!')
    return False


if __name__ == '__main__':
    guess(300, 50)