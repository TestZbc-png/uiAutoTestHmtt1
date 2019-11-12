import time

import pytest

import utils
from page.mis.login_page import LoginProxy
from utils import DriverUtil

@pytest.mark.run(order=2)
class TestLogin():

    def setup_class(self):
        self.login = LoginProxy()


    def teardown_class(self):
        time.sleep(3)


    def test_login_success(self):
        username = "testid"
        pwd = "testpwd123"
        nickname = "管理员"

        self.login.click_to_login(username, pwd)

        # 断言
        is_exit = utils.exist_text(DriverUtil.get_mis_driver(), nickname)
        assert is_exit