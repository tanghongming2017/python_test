# coding=utf-8
import os


class PathUtil:

    @staticmethod
    def get_root_path():
        """
            获取项目根目录
        """
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        return root_path

    @staticmethod
    def get_file_path(abs_file_path):
        """
            将相对路径转换成文件绝对路径
        """
        return os.path.join(PathUtil.get_root_path(), abs_file_path)


if __name__ == '__main__':
    """测试"""
    print(PathUtil.getRootPath())
