# coding=utf-8
from selenium import webdriver
from business.register_ddt_business import RegisterDDTBusiness
import unittest
from util.html_test_runner import HTMLTestRunner
from ddt import *
from util.excel_util import ExcelUtil
from util.path_util import PathUtil

excel_util = ExcelUtil(PathUtil.get_file_path("conf/case.xls"))
datas = excel_util.get_data()


@ddt
class RegisterDDTCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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
    file_path = PathUtil.get_file_path("report/RegisterDDTReport.html")
    f = open(file_path, 'wb')
    html_test = HTMLTestRunner(stream=f, title='RegisterDDTReport', description='这是一个注册页面的报告')
    html_test.run(testSuite)
