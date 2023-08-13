import logging

logging.basicConfig(
    filename='log.log',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}',
    style='{',
    level=logging.WARNING
)

def div():
    logger = logging.getLogger('main')
    logger.warning('Делить на 0 нельзя')
    return 5/0


if __name__ == '__main__':
    div()
