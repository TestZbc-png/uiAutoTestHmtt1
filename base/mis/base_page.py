from utils import DriverUtil

class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_mis_driver()

    def find_element(self, location):
        return self.driver.find_element(location[0], location[1])

class BaseHandle:
    # 输入操作
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

