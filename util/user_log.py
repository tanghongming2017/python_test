# coding=utf-8
import logging
import datetime
from util.path_util import PathUtil


class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        log_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_path = PathUtil.get_file_path(f"logs/{log_name}")
        # 文件输出
        self.file_handle = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelno)s %(levelname)s %(message)s')
        self.file_handle.setFormatter(formatter)
        self.file_handle.setLevel(logging.INFO)
        self.logger.addHandler(self.file_handle)

    def get_logger(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()
