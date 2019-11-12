from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        # 信息管理
        self.indo_manage = By.LINK_TEXT, "信息管理"
        # 内容管理
        self.content_audit = By.LINK_TEXT, "内容审核"

    def find_info_manage(self):
        return self.find_element(self.indo_manage)

    def find_content_audit(self):
        return self.find_element(self.content_audit)

class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    def click_info_manage(self):
        self.home_page.find_info_manage().click()

    def click_content_audit(self):
        self.home_page.find_content_audit().click()

class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def click_to_audit_page(self):
        self.home_handle.click_info_manage()
        self.home_handle.click_content_audit()

