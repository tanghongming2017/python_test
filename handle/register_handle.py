# coding=utf-8
from page.register_page import RegisterPage
from PIL import Image

class RegisterHandle:

    def __init__(self, driver):
        self.driver = driver
        self.register_page = RegisterPage(driver)

    # 发送username的值
    def send_username_element(self, value):
        self.register_page.get_username_element().send_keys(value)

    # 发送password的值
    def send_password_element(self, value):
        self.register_page.get_password_element().send_keys(value)

    # 发送password2的值
    def send_password2_element(self, value):
        self.register_page.get_password2_element().send_keys(value)

    # 发送email的值
    def send_email_element(self, value):
        self.register_page.get_email_element().send_keys(value)

    # 发送answer的值
    def send_answer_element(self, value):
        self.register_page.get_answer_element().send_keys(value)

    # 裁剪后的验证码图片元素
    def crop_vcode_img_element(self, file_name):
        element = self.register_page.get_vcode_img_element()
        self.driver.save_screenshot(file_name)
        left = element.location['x']
        top = element.location['y']
        right = left + element.size['width']
        bottom = top + element.size['height']
        im = Image.open(file_name)
        code_img = im.crop((left, top, right, bottom))
        code_img.save(file_name)

    # 发送code值
    def send_vcode_element(self, value):
        self.register_page.get_vcode_element().send_keys(value)

    # 获取登录按钮元素
    def click_login_btn_element(self):
        self.register_page.get_login_btn_element().click()

    # 对比报错js弹框内容，并关闭弹框
    def compare_alert_text(self, text):
        result = False
        try:
            alert_element = self.register_page.get_alert_element()
            result = alert_element.text == text
            alert_element.accept()
        except:
            pass
        finally:
            return result
