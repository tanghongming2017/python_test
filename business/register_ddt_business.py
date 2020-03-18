# coding=utf-8
import time

from handle.register_handle import RegisterHandle
from util.common_util import *
from selenium.webdriver.support import expected_conditions as EC

from util.path_util import PathUtil


class RegisterDDTBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.register_handle = RegisterHandle(driver)
        self.file_name = PathUtil.get_file_path("img/code.png")

    def register_main(self, username, password, password2, email, answer, vcode, assert_text):
        self.register_handle.send_username_element(username)
        if vcode == '' or vcode is None:
            self.register_handle.crop_vcode_img_element(self.file_name)
            code = get_code_text(self.file_name)
            self.register_handle.send_vcode_element(code.strip())
        else:
            self.register_handle.send_vcode_element(vcode)
        self.register_handle.send_password_element(password)
        self.register_handle.send_password2_element(password2)
        self.register_handle.send_email_element(email)
        self.register_handle.send_answer_element(answer)
        self.register_handle.click_login_btn_element()
        if self.register_handle.compare_alert_text(assert_text):
            return True
        time.sleep(5)
        return self.is_home_page(assert_text)

    def is_home_page(self, url):
        return EC.url_contains(url)(self.driver)
