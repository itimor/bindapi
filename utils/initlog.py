# -*- coding: utf-8 -*-
# author: itimor
import logging


def initlog(logfile):
    """
    创建日志实例
    """
    logger = logging.getLogger()
    hdlr = logging.FileHandler(logfile, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt='%m-%d-%Y %I:%M:%S')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.WARNING)
    return logger


def InitLogging(logfile):
    logging.basicConfig(
                        handlers=[logging.FileHandler(logfile, 'a', 'utf-8')],
                        level=logging.WARNING,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt='%m-%d-%Y %I:%M:%S'
                        )


def LoggingDemo():
    logging.debug("this is debug message")
    logging.info("this is info message")
    logging.warning("this is warning message")
    logging.error("this is error message")
    domain = 'xxoo.com'
    result = {'rr': 13, '232': 321}
    logging.warning("ip已经自动更换 %s %s" % (domain, result))


if __name__ == '__main__':
    InitLogging('./test.log')
    LoggingDemo()
