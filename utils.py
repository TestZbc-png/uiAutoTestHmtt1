# 封装驱动的工具类
import time
import appium.webdriver
from selenium import webdriver
import config
import logging

# 处理下拉选择框
def select_by_option(driver, element, option_name):
    element.click()
    time.sleep(3)
    xpath = "//*[@class='el-scrollbar']//*[text()='{}']".format(option_name)
    driver.find_element_by_xpath(xpath).click()

# 判断当前页面中是否包含指定的文字
# 存在：True， 不存在:False
def exist_text(driver, text):
    try:
        xpath = "//*[contains(text(), '{}')]".format(text)
        ele  = driver.find_element_by_xpath(xpath)
        return True
    except Exception as e:
        # traceback.print_exc()
        logging.exception(e)
        # print("current page is not contains text=[{}]".format(text))
        logging.error("current page is not contains text=[{}]".format(text))
        return False
# 获取APP包名的命令：adb logcat|findstr Displayed
class DriverUtil:
    _mp_driver = None
    _mis_driver = None
    _app_driver = None

    _mp_auto_quit = True

    # 自媒体：mp
    # 获取驱动
    @classmethod
    def get_mp_driver(cls):
        if cls._mp_driver is None:
            cls._mp_driver = webdriver.Chrome()
            cls._mp_driver.maximize_window()
            cls._mp_driver.implicitly_wait(10)
            cls._mp_driver.get(config.MP_BASE_URL)

        return cls._mp_driver

    # 获取关闭驱动
    @classmethod
    def get_mp_quit(cls) :
        if cls._mp_driver is not None and cls._mp_auto_quit:
            cls._mp_driver.quit()
            cls._mp_driver = None

    # 设置开关
    @classmethod
    def set_mp_auto_quit(cls, auto_quit):
        cls._mp_auto_quit = auto_quit


# 后台管理系统
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.implicitly_wait(10)
            cls._mis_driver.get('http://ttmis.research.itcast.cn/')
        return cls._mis_driver

# 关闭驱动
    @classmethod
    def get_mis_quit(cls):
        if cls._mis_driver is not None:
            cls._mis_driver.quit()
            cls._mis_driver = None

# APP
    # 获取驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            cap = {
                "platformName": "Android",
                "deviceName": "em",
                "appPackage": "com.itcast.toutiaoApp",
                "appActivity": ".MainActivity",
                "noReset": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True
            }
            cls._app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            cls._app_driver.implicitly_wait(10)
        return cls._app_driver

    # 关闭驱动
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls._app_driver.quit()