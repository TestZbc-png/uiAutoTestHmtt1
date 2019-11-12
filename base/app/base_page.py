from utils import DriverUtil

# 对象库层类
class BasePage:
    def __init__(self):
        self.driver = DriverUtil.get_app_driver()

    # 定位元素
    def find_element(self, loc):
        return self.driver.find_element_by_id(loc[0], loc[1])

    # 边滑动边定位元素


# 操作层父类
class BaseHandle:

    # 输入操作
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)