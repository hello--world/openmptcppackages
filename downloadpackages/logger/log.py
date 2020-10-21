# import os
# import logging
# import logging.config as log_conf

# log_dir = '/data/logs'
# if not os.path.exists(log_dir):
#     os.mkdir(log_dir)
# pip install ConcurrentLogHandler
from logging import getLogger, INFO, Formatter, StreamHandler
from cloghandler import ConcurrentRotatingFileHandler

def get_logger(logfile, name, level=INFO, maxSzie_M=1024, backupCount=15, console=True):
    '''
    获取多进程日志
    :param logfile:
    :param name:
    :param level:
    :param maxSzie_M: 按M计算
    :param backupCount: 多少个备份文件
    :return:
    '''
    _log = getLogger(name)
    _log.setLevel(level)

    # logfile = os.path.abspath('logs/upload.log')
    rotateHandler = ConcurrentRotatingFileHandler(logfile, 'a', 1024 * 1024 * maxSzie_M, backupCount, encoding='utf-8')
    # formatter = logging.Formatter(
    #         fmt="%(asctime)s %(levelname)s: %(name)s %(filename)s:%(lineno)d %(message)s",
    #         datefmt="%Y-%m-%d %X"
    #         )
    datefmt_str = '%Y-%m-%d %H:%M:%S'
    format_str = "%(asctime)s %(levelname)s: %(name)s %(filename)s:%(lineno)d %(message)s"
    formatter = Formatter(format_str, datefmt_str)
    rotateHandler.setFormatter(formatter)
    rotateHandler.setLevel(level)

    if console:
        _console = StreamHandler()
        _console.setFormatter(formatter)
        _console.setLevel(INFO)
        _log.addHandler(_console)

    _log.addHandler(rotateHandler)

    return _log
