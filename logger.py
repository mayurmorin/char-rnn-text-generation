import logging
from logging.handlers import RotatingFileHandler
from os import path


def get_logger(name, log_path=path.join(path.dirname(__file__), "main.log"), console=False):
    """
    Simple logging wrapper that returns logger
    configured to log into file and console.
    Args:
        name (str): name of logger
        log_path (str): path of log file
        console (bool): whether to log on console
    Returns:
        logging.Logger: configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # ensure that logging handlers are not duplicated
    for handler in logger.handlers.copy():
        logger.removeHandler(handler)

    # rotating file handler
    if log_path:
        fh = RotatingFileHandler(log_path,
                                 maxBytes=2 ** 20,  # 1 MB
                                 backupCount=1)  # 1 backup
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    # console handler
    if console:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    # null handler
    if not (log_path or console):
        logger.addHandler(logging.NullHandler())

    return logger