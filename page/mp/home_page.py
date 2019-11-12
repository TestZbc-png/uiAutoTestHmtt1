import time

from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage
from base.mp.base_page import BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 内容管理
        self.content_manage = By.XPATH, "//ul[@role='menubar']//*[text()='内容管理']"
        # 发布文章
        self.publish_menu = (By.XPATH, "//ul[@role='menubar']//*[contains(text(), '发布文章')]")

    def find_content_manage(self):
        return self.find_element(self.content_manage)

    def find_publish_manage(self):
        return self.find_element(self.publish_menu)

class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    def click_conten_manage(self):
        self.home_page.find_content_manage().click()


    def click_publish_menu(self):
        self.home_page.find_publish_manage().click()


class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    def to_article_page(self):
        self.home_handle.click_conten_manage()
        self.home_handle.click_publish_menu()
        time.sleep(6)












