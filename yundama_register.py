import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
import time
from aip import AipOcr
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.find_element import FindElement

file_path = os.path.join(os.path.dirname(os.getcwd()),'driver/chromedriver.exe')
wb = webdriver.Chrome(file_path)
password = 'test_zhangsan'
answer_result = 'zhangsanfeng'
find_element = FindElement(wb)


def init_webdriver():
    wb.get("http://www.yundama.com/index/reg")
    wb.maximize_window()


def web_wait(element):
    WebDriverWait(wb, 2).until(EC.visibility_of(element))


def get_user_name():
    return random.sample('1234567890abcdefg', 10)


def get_code_img(element, file_name):
    wb.save_screenshot(file_name)
    left = element.location['x']
    top = element.location['y']
    right = left + element.size['width']
    bottom = top + element.size['height']
    im = Image.open(file_name)
    code_img = im.crop((left, top, right, bottom))
    code_img.save(file_name)


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


def login():
    file_name = "img/code.png"
    code_text = None
    count = 0

    while code_text is None and count <= 10:
        count += 1
        print("验证码流程开始")
        vcode_img_element = find_element.get_element("RegisterElement", "vcode_img")
        vcode_img_element.click()
        time.sleep(3)
        get_code_img(vcode_img_element, file_name)
        code_text = get_code_text(file_name)
        print(f"第{count}次识别验证码，识别的结果为：{code_text}")
        print("验证码流程结束")
        if code_text is None:
            continue
        code_element = find_element.get_element("RegisterElement", "vcode")
        web_wait(code_element)
        code_element.clear()
        code_element.send_keys(code_text.strip())
        login_btn_element = find_element.get_element("RegisterElement", "login_btn")
        web_wait(login_btn_element)
        login_btn_element.click()
        time.sleep(5)
        try:
            wb.switch_to.alert.accept()
        except:
            pass

        if EC.url_contains("http://www.yundama.com/user")(wb):
            user_info_element = find_element.get_element("HomeElement", "user_info")
            user_info = user_info_element.get_attribute("text")
            if user_info == username:
                print("登录成功")
            else:
                print("登录失败")
            break
        else:
            code_text = None


if __name__ == '__main__':
    try:
        init_webdriver()
        if EC.title_contains('用户注册')(wb):
            username = "".join(get_user_name())
            email = username + "@163.com"
            username_element = find_element.get_element("RegisterElement", "username")
            web_wait(username_element)
            username_element.send_keys(username)
            password_element = find_element.get_element("RegisterElement", "password")
            web_wait(password_element)
            password_element.send_keys(password)
            password_repeat_element = find_element.get_element("RegisterElement", "password2")
            web_wait(password_repeat_element)
            password_repeat_element.send_keys(password)

            email_element = find_element.get_element("RegisterElement", "email")
            web_wait(email_element)
            email_element.send_keys(email)

            aq_answer_element = find_element.get_element("RegisterElement", "aq_answer")
            web_wait(aq_answer_element)
            aq_answer_element.send_keys(answer_result)

            login()
    except Exception as e:
        print(e)
    finally:
        wb.close()
