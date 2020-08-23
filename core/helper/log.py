import logging


def setup_custom_logger(name):
    logging.basicConfig(filename='malamute.log', level=logging.DEBUG)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


malamute_logger = setup_custom_logger('malamute')


