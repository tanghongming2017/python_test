# coding=utf-8
import time

from handle.register_handle import RegisterHandle
from util.common_util import *
from selenium.webdriver.support import expected_conditions as EC
from util.path_util import PathUtil


class RegisterBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.register_handle = RegisterHandle(driver)
        self.file_name = PathUtil.get_file_path("img/code.png")

    # 输入错误的用户名
    def send_username_error(self, username):
        self.register_handle.send_username_element(username)
        self.register_handle.click_login_btn_element()
        return self.register_handle.compare_alert_text('注册失败！用户名长度必须6位以上15位以下且字母开头')

    # 手工输入验证码
    def send_code_error(self, username, code):
        self.register_handle.send_username_element(username)
        self.register_handle.send_vcode_element(code)
        self.register_handle.click_login_btn_element()
        return self.register_handle.compare_alert_text('注册失败！验证码输入错误')

    # 自动识别验证码图像成功
    def send_code_success(self, username):
        if not self.send_username_error(username):
            self.register_handle.crop_vcode_img_element(self.file_name)
            code = get_code_text(self.file_name)
            self.register_handle.send_vcode_element(code.strip())
            self.register_handle.click_login_btn_element()
            return not self.register_handle.compare_alert_text('注册失败！验证码输入错误')
        return False

    # 输入错误的密码
    def send_password_error(self, username, password):
        if self.send_code_success(username):
            self.register_handle.send_password_element(password)
            self.register_handle.click_login_btn_element()
            return self.register_handle.compare_alert_text('注册失败！密码长度必须6位以上')
        return False

    # 输入重复密码的错误密码
    def send_password2_error(self, username, password, password2):
        if self.send_code_success(username):
            self.register_handle.send_password_element(password)
            self.register_handle.send_password2_element(password2)
            self.register_handle.click_login_btn_element()
            return self.register_handle.compare_alert_text('注册失败！两次密码输入不一致')
        return False

    # 输入错误的邮箱
    def send_email_error(self, username, password, password2, email):
        if self.send_code_success(username):
            self.register_handle.send_password_element(password)
            self.register_handle.send_password2_element(password2)
            self.register_handle.send_email_element(email)
            self.register_handle.click_login_btn_element()
            return self.register_handle.compare_alert_text('注册失败！邮箱输入有误')
        return False

    # 输入错误的问题答案
    def send_answer_error(self, username, password, password2, email, answer):
        if self.send_code_success(username):
            self.register_handle.send_password_element(password)
            self.register_handle.send_password2_element(password2)
            self.register_handle.send_email_element(email)
            self.register_handle.send_answer_element(answer)
            self.register_handle.click_login_btn_element()
            return self.register_handle.compare_alert_text('注册失败！密保答案不能为空')
        return False

    # 正常注册流程
    def register(self, username, password, password2, email, answer):
        self.register_handle.send_username_element(username)
        self.register_handle.crop_vcode_img_element(self.file_name)
        code = get_code_text(self.file_name)
        self.register_handle.send_password_element(password)
        self.register_handle.send_password2_element(password2)
        self.register_handle.send_email_element(email)
        self.register_handle.send_answer_element(answer)
        self.register_handle.send_vcode_element(code.strip())
        self.register_handle.click_login_btn_element()
        if self.register_handle.compare_alert_text('注册失败！验证码输入错误'):
            return False
        time.sleep(5)
        return self.is_home_page()

    def is_home_page(self):
        return EC.url_contains("http://www.yundama.com/user")(self.driver)
