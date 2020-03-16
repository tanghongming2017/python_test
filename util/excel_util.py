
import os

import xlrd
from xlutils.copy import copy


class ExcelUtil:
    def __init__(self, file_path, index=0):
        self.file_path = file_path
        self.index = index
        data = xlrd.open_workbook(file_path)
        self.book_sheet = data.sheet_by_index(index)

    def get_data(self):
        data = []
        for i in range(self.get_lines()):
            data.append(self.book_sheet.row_values(i))
        return data

    def get_lines(self):
        return self.book_sheet.nrows

    # 获取单元格的数据
    def get_cell_value(self, row, col):
        if self.get_lines() > row:
            return self.book_sheet.cell_value(row, col)
        else:
            return None

    # 写入数据
    def write_cell_value(self, row, col, value):
        data = xlrd.open_workbook(self.file_path)
        write_data = copy(data)
        sheet = write_data.get_sheet(self.index)
        sheet.write(row, col, value)
        write_data.save(self.file_path)


if __name__ == '__main__':
    file_path = "conf/keyword.xls"
    execl = ExcelUtil(file_path)
    data = execl.get_cell_value(1, 4)
    print(data)
    execl.write_cell_value(1, 6, "hello world")

