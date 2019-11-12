import time
from selenium.webdriver.common.by import By

import utils
from base.mis.base_page import BasePage, BaseHandle


class ArticleAuditPage(BasePage):
    def __init__(self):
        super().__init__()
        # 标题
        self.title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
        # 文章状态
        self.status = By.CSS_SELECTOR, "[placeholder='请选择状态']"
        # 查询按钮
        self.query_btn = By.CLASS_NAME, "find"
        # 通过按钮
        # 或者通过文章的标题进行定位：//*[text()='test001']/../..//*[text()='通过']
        self.pass_btn = By.XPATH, "//span[text()='通过']/.."
        # 确认按钮
        self.confirm_btn = By.CLASS_NAME, "el-button--primary"

    def find_title(self):
        return self.find_element(self.title)

    def find_status(self):
        return self.find_element(self.status)

    def find_quer_btn(self):
        return self.find_element(self.query_btn)

    def find_pass_btn(self):
        return self.find_element(self.pass_btn)

    def find_confirm_btn(self):
        return self.find_element(self.confirm_btn)


class ArticleAuditHandle(BaseHandle):
    def __init__(self):
        self.audit_page = ArticleAuditPage()
        self.driver = utils.DriverUtil.get_mis_driver()

    def input_title(self, title):
        self.input_text(self.audit_page.find_title(), title)

    def select_status(self, status):
        utils.select_by_option(self.driver, self.audit_page.find_status(), status)

    def click_query_btn(self):
        self.audit_page.find_quer_btn().click()

    def click_pass_btn(self):
        self.audit_page.find_pass_btn().click()

    def click_confirm_btn(self):
        self.audit_page.find_confirm_btn().click()


class ArticleAuditProxy:

    def __init__(self):
        self.audit_handle = ArticleAuditHandle()
        self.driver = utils.DriverUtil.get_mis_driver()

    def click_to_article_audit(self, title, status):
        self.audit_handle.input_title(title)
        self.audit_handle.select_status(status)
        self.audit_handle.click_query_btn()
        self.audit_handle.click_pass_btn()
        self.audit_handle.click_confirm_btn()

    # 判断文章审核是否通过
    def is_pass_audit(self, title):
        self.driver.refresh()
        self.audit_handle.input_title(title)
        self.audit_handle.select_status("审核通过")
        self.audit_handle.click_query_btn()
        time.sleep(3)
        is_exit = utils.exist_text(utils.DriverUtil.get_mis_driver(), title)
        return is_exit

