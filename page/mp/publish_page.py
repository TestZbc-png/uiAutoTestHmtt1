import time

from selenium.webdriver.common.by import By

import utils
from base.mp.base_page import BasePage, BaseHandle


class PublishPage(BasePage):
    def __init__(self):
        super().__init__()
        # 标题
        self.title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # 内容frame
        self.content_frame = (By.ID, "publishTinymce_ifr")
        # 内容
        self.content = (By.TAG_NAME, "body")
        # 封面(元素被挡住，采取上级目录去定位)
        # self.cover = (By.CSS_SELECTOR, "input[value='auto']")
        # self.cover = (By.XPATH, "//input[@value='auto']")
        self.cover = (By.XPATH, "//input[@value='auto']/..")
        # self.cover = (By.XPATH, "//*[contains(text(), '自动')]")
        # 频道
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道 - 数据库
        self.channel_db = (By.XPATH, "//*[@class='el-scrollbar']//*[text()='数据库']")
        # 发布按钮
        self.publish_btn = (By.CLASS_NAME, "el-button--primary")

    def find_title(self):
        return self.find_element(self.title)

    def find_conten_frame(self):
        return self.find_element(self.content_frame)

    def find_conten(self):
        return self.find_element(self.content)

    def find_cover(self):
        return self.find_element(self.cover)

    def find_channel(self):
        return self.find_element(self.channel)

    def find_publish_btn(self):
        return self.find_element(self.publish_btn)


class PublishHandle(BaseHandle):
    def __init__(self):
        self.publish_page = PublishPage()
        self.driver = utils.DriverUtil

    def input_title(self, title):
        self.input_text(self.publish_page.find_title(), title)

    def input_conten(self, content):
        # 跳转iframe页面
        self.driver.get_mp_driver().switch_to.frame(self.publish_page.find_conten_frame())
        self.input_text(self.publish_page.find_conten(), content)
        self.driver.get_mp_driver().switch_to.default_content()
    def click_over(self):
        self.publish_page.find_cover().click()

    def select_channel(self, channel):
        utils.select_by_option(self.driver.get_mp_driver(), self.publish_page.find_channel(), channel)

    def click_publish_btn(self):
        self.publish_page.find_publish_btn().click()


class PublishProxy:
    def __init__(self):
        self.handle = PublishHandle()

    def publish_article(self, title, content, channel):
        self.handle.input_title(title)
        time.sleep(3)
        self.handle.input_conten(content)
        self.handle.click_over()
        self.handle.select_channel(channel)
        time.sleep(3)
        self.handle.click_publish_btn()
