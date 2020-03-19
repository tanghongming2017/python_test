# coding=utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from business.register_business import RegisterBusiness
from util.common_util import *
import unittest
from util.html_test_runner import HTMLTestRunner

from util.user_log import UserLog
from util.path_util import PathUtil


class RegisterCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_log = UserLog()
        cls.user_log.get_logger().info("类前置")

    @classmethod
    def tearDownClass(cls):
        cls.user_log.get_logger().info("类后置")
        cls.user_log.close_handle()

    def setUp(self):
        self.user_log.get_logger().info("setUp")
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://www.yundama.com/index/reg")
        self.driver.maximize_window()
        self.register_business = RegisterBusiness(self.driver)

    def tearDown(self):
        self.user_log.get_logger().info("tearDown")
        self.driver.close()

    def test_register_username_error(self):
        self.assertTrue(self.register_business.send_username_error("1"), "【test_register_username_error】执行不通过")

    def test_register_password_error(self):
        username = get_user_name()
        self.assertTrue(self.register_business.send_password_error(username, '1'),
                        "【test_register_password_error】执行不通过")

    def test_register_password2_error(self):
        username = "".join(get_user_name())
        self.assertTrue(self.register_business.send_password2_error(username, '123456', '1234'),
                        "【test_register_password2_error】执行不通过")

    def test_register_email_error(self):
        username = "".join(get_user_name())
        password = '123456'
        self.assertTrue(self.register_business.send_email_error(username, password, password, '123'),
                        "【test_register_email_error】执行不通过")

    def test_register_answer_error(self):
        username = "".join(get_user_name())
        email = username + "@qq.com"
        password = '123456'
        self.assertTrue(self.register_business.send_answer_error(username, password, password, email, ' '),
                        "【test_register_answer_error】执行不通过")

    def test_register_code_error(self):
        username = "".join(get_user_name())
        self.assertTrue(self.register_business.send_code_error(username, '1234'), "【test_register_code_error】执行不通过")

    def test_login_success(self):
        username = "".join(get_user_name())
        email = username + "@qq.com"
        password = '123456'
        answer = 'zhangsan'
        self.assertTrue(self.register_business.register(username, password, password, email, answer),
                        "【test_login_success】执行不通过")

    def main(self):
        testSuite = unittest.TestSuite()
        testSuite.addTest(RegisterCase('test_register_code_error'))
        testSuite.addTest(RegisterCase('test_login_success'))
        file_path = PathUtil.get_file_path("report/RegisterReport.html")
        f = open(file_path, 'wb')
        html_test = HTMLTestRunner(stream=f, title='RegisterReport', description='这是一个注册页面的报告')
        html_test.run(testSuite)


if __name__ == '__main__':
    RegisterCase().main()
