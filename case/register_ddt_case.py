# coding=utf-8
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from selenium import webdriver
from business.register_ddt_business import RegisterDDTBusiness
import unittest
from util.html_test_runner import HTMLTestRunner
from ddt import *
from util.excel_util import ExcelUtil

excel_util = ExcelUtil(os.path.join(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__)))), "conf/case.xls"))
datas = excel_util.get_data()

@ddt
class RegisterDDTCase(unittest.TestCase):

    def setUp(self):
        file_path = webdriver.Chrome('C:\\Users\\TEST\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver = webdriver.Chrome(file_path)
        self.driver.get("http://www.yundama.com/index/reg")
        self.driver.maximize_window()
        self.register_business = RegisterDDTBusiness(self.driver)

    def tearDown(self):
        self.driver.close()

    @data(*datas)
    def test_register_success(self, datas):
        username, password, password2, email, answer, code, assert_text = datas
        self.assertTrue(
            self.register_business.register_main(username, password, password2, email, answer, code, assert_text),
            assert_text)


if __name__ == '__main__':
    testSuite = unittest.TestLoader().loadTestsFromTestCase(RegisterDDTCase)
    file_path = os.path.join(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__)))),
                             "report/RegisterDDTReport.html")
    f = open(file_path, 'wb')
    html_test = HTMLTestRunner(stream=f, title='RegisterDDTReport', description='这是一个注册页面的报告')
    html_test.run(testSuite)
