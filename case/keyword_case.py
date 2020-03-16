# coding=utf-8
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from util.excel_util import ExcelUtil
from util.action_method import ActionMethod


class KeywordCase:

    def run_main(self):
        file_path = os.path.join(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__)))), "conf/keyword.xls")
        excel = ExcelUtil(file_path)
        rows = excel.get_lines()
        action_method = ActionMethod()
        for i in range(1, rows):
            is_run = excel.get_cell_value(i, 1)
            if is_run == 'Y':
                node_element = excel.get_cell_value(i, 3)
                exec_method = excel.get_cell_value(i, 4)
                send_value = excel.get_cell_value(i, 5)
                action_element = excel.get_cell_value(i, 6)
                except_result_method = excel.get_cell_value(i, 7)
                except_result = excel.get_cell_value(i, 8)
                self.run_method(action_method, exec_method, node_element, action_element, send_value)
                if except_result_method != '' and except_result != '':
                    result = self.exec_result_method(action_method, except_result_method)
                    if except_result in result:
                        excel.write_cell_value(i, 9, 'pass')
                    else:
                        excel.write_cell_value(i, 9, 'fail')

    def exec_result_method(self, action_method, except_result_method):
        return getattr(action_method, except_result_method)()

    def run_method(self, action_method, exec_method, node_element, action_element, send_value):
        method_value = getattr(action_method, exec_method)
        if send_value != '' and action_element != '':
            method_value(node_element, action_element, send_value)
        elif send_value == '' and action_element != '':
            method_value(node_element, action_element)
        elif send_value != '' and action_element == '':
            method_value(send_value)
        else:
            method_value()


if __name__ == '__main__':
    keyword_case = KeywordCase()
    keyword_case.run_main()
