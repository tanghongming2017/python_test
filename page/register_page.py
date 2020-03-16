# coding=utf-8
from page.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # 获取用户名元素
    def get_username_element(self):
        return self.get_element("RegisterElement", "username")

    # 获取密码元素
    def get_password_element(self):
        return self.get_element("RegisterElement", "password")

    # 获取再次输入密码元素
    def get_password2_element(self):
        return self.get_element("RegisterElement", "password2")

    # 获取邮箱元素
    def get_email_element(self):
        return self.get_element("RegisterElement", "email")

    # 获取回答问题元素
    def get_answer_element(self):
        return self.get_element("RegisterElement", "aq_answer")

    # 获取验证码图片元素
    def get_vcode_img_element(self):
        return self.get_element("RegisterElement", "vcode_img")

    # 获取验证码输入框元素
    def get_vcode_element(self):
        return self.get_element("RegisterElement", "vcode")

    # 获取登录按钮元素
    def get_login_btn_element(self):
        return self.get_element("RegisterElement", "login_btn")
