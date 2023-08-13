import os
import logging
from collections import namedtuple

logging.basicConfig(
    filename='dir.log',
    encoding='utf-8',
    format='{levelname} {funcName} -> {msg}',
    style='{',
    level=logging.INFO
)


def name_directory(folder: str):
    Result = namedtuple('dir', 'name ext flag dir')
    logger = logging.getLogger('main')
    result_list = []
    os.chdir(folder)
    file_list = os.listdir(folder)
    for i in range(len(file_list)):
        if os.path.isdir(file_list[i]):
            name, ext, flag = file_list[i], '', 'dir'
        else:
            name, ext = file_list[i].split('.')
            flag = 'notdir'
        res = Result(name, ext, flag, folder)
        result_list.append(res)
        logger.info(f'{res}')


if __name__ == '__main__':
    folder = 'C:\\Users\\kabaa\\Desktop\\Файлы'
    name_directory(folder)
