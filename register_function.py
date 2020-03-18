# coding=utf-8
import random
import time

from PIL import Image
from aip import AipOcr
from selenium import webdriver
from base.find_element import FindElement
from selenium.webdriver.support import expected_conditions as EC

from util.path_util import PathUtil


def get_user_name():
    return random.sample('1234567890abcdefg', 10)


def get_code_text(file_name):
    """ 你的 APPID AK SK """
    APP_ID = '18775449'
    API_KEY = 'HcIsOvfEixU2DEjdyL6fFhDB'
    SECRET_KEY = 'K6BXnPr2Xw0vB3HFzdjwZ0KWSUvAxdhr'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    with open(file_name, 'rb') as fp:
        img = fp.read()
        result = client.basicAccurate(img)
        print("aip识别结果为：", result)
        if result is not None and result['words_result_num'] > 0:
            return result['words_result'][0]['words']
    return None


class RegisterFunction:
    def __init__(self, url):
        self.driver = self.get_driver(url)
        self.find_element = FindElement(self.driver)

    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def _get_element(self, node_element, element):
        return self.find_element.get_element(node_element, element)

    def send_keys(self, element, value, node_element="RegisterElement"):
        element = self._get_element(node_element, element)
        element.clear()
        element.send_keys(value)

    def click(self, element, node_element="RegisterElement"):
        self._get_element(node_element, element).click()

    def get_code_img(self, element, file_name):
        self.driver.save_screenshot(file_name)
        left = element.location['x']
        top = element.location['y']
        right = left + element.size['width']
        bottom = top + element.size['height']
        im = Image.open(file_name)
        code_img = im.crop((left, top, right, bottom))
        code_img.save(file_name)

    def save_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def alert_accept(self):
        # 这里加异常判断是防止抛异常后程序不再向后执行，这里不做处理
        try:
            self.driver.switch_to.alert.accept()
        except:
            pass

    def is_home_page(self):
        return EC.url_contains("http://www.yundama.com/user")(self.driver)

    def main(self):
        username = "".join(get_user_name())
        email = username + "@163.com"
        password = 'test_zhangsan'
        answer_result = 'zhangsanfeng'

        self.send_keys("username", username)
        self.send_keys("password", password)
        self.send_keys("password2", password)
        self.send_keys("email", email)
        self.send_keys("aq_answer", answer_result)
        file_name = PathUtil.get_file_path("img/code.png")
        code_text = None
        count = 0

        while code_text is None and count <= 10:
            count += 1
            print("验证码流程开始")
            self.click("vcode_img")
            time.sleep(3)
            self.get_code_img(self._get_element("RegisterElement", "vcode_img"), file_name)
            code_text = get_code_text(file_name)
            print(f"第{count}次识别验证码，识别的结果为：{code_text}")
            print("验证码流程结束")
            if code_text is None:
                continue
            self.send_keys("vcode", code_text.strip())
            self.click("login_btn")
            time.sleep(5)
            self.alert_accept()

            if self.is_home_page():
                user_info = self._get_element("HomeElement", "user_info").get_attribute("text")
                if user_info == username:
                    print("登录成功")
                else:
                    print("登录失败")
                    file_path = PathUtil.get_file_path("img/fail_screenshot.png")
                    self.save_screenshot(file_path)
                break
            else:
                code_text = None


if __name__ == '__main__':
    try:
        RegisterFunction("http://www.yundama.com/index/reg").main()
    except Exception as e:
        print("程序出现异常啦~~~", e)
