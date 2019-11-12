from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle

print()
print()
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        # 手机号
        self.mobile = (By.CSS_SELECTOR, "input[placeholder='请输入手机号']")
        # 验证码
        self.code = (By.CSS_SELECTOR, "input[placeholder='验证码']")
        # 登录按钮
        self.login_btn = (By.CLASS_NAME, "el-button--primary")

    # 手机输入框
    def find_mobile(self):
        return self.find_element(self.mobile)

    # 验证码
    def find_code(self):
        return self.find_element(self.code)

    # 登录按钮
    def find_login_btn(self):
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 输入手机号
    def input_moblie(self, moblie):
        self.input_text(self.login_page.find_mobile(), moblie)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登录

    def click_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    def click_login(self, mobile, code):
        self.login_handle.input_moblie(mobile)
        self.login_handle.input_code(code)
        self.login_handle.click_btn()
