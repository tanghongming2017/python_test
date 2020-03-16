
from util.read_ini import ReadIni


class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, node_element, element):
        try:
            read_ini = ReadIni()
            data = read_ini.get_value(node_element, element)
            by = data.split('>')[0]
            value = data.split('>')[1]
            result = self.driver.find_element(by, value)
        except:
            result = None
        return result
