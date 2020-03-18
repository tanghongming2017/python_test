# coding=utf-8
import configparser

from util.path_util import PathUtil


class ReadIni:
    """
    读取配置文件
    """

    def __init__(self, file_name=None):
        if not file_name:
            file_name = PathUtil.get_file_path("conf/element.ini")
        self.cf = self._load_ini(file_name)

    def _load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf

    def get_value(self, node_element, element):
        """
        获取节点的值
        :param node_element:
        :param element:
        :return:
        """
        return self.cf.get(node_element, element)
