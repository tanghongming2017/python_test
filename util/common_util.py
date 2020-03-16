
import random

from aip import AipOcr


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
    return ""


def get_user_name():
    return random.sample('1234567890abcdefg', 10)
