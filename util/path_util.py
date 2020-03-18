# coding=utf-8
import sys
import os


class PathUtil:

    @staticmethod
    def get_root_path():
        """
            获取项目根目录
        """
        # 判断调试模式
        debug_vars = dict((a, b) for a, b in os.environ.items() if a.find('IPYTHONENABLE') >= 0)
        # 根据不同场景获取根目录
        if len(debug_vars) > 0:
            # 当前为debug运行时
            rootPath = sys.path[2]
        elif getattr(sys, 'frozen', False):
            # 当前为exe运行时
            rootPath = os.getcwd()
        else:
            # 正常执行
            rootPath = sys.path[1]
        # 替换斜杠
        rootPath = rootPath.replace("\\", "/")
        return rootPath

    @staticmethod
    def get_file_path(abs_file_path):
        """
            将相对路径转换成文件绝对路径
        """
        return os.path.join(PathUtil.get_root_path(), abs_file_path)


if __name__ == '__main__':
    """测试"""
    print(PathUtil.getRootPath())
