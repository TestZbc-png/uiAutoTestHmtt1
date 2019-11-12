import json
import logging
import time
import pytest
import config
import utils
from page.mp.login_page import LoginProxy
from utils import DriverUtil


def build_data():
    test_data = []
    with open(config.BASE_DIR + "/data/mp/login.json", encoding="utf-8") as f:
        json_data = json.load(f)
        test_login_data = json_data.get('test_login')
        for case_data in test_login_data:
            mobile = case_data.get("mobile")
            code = case_data.get("code")
            username = case_data.get("username")
            test_data.append((mobile, code, username))
    # print("test_data=", test_data)
    logging.info("test_data".format(test_data))
    return test_data

@pytest.mark.run(order=2)
class TestLogin:

    def setup_class(self):
        self.login_proxy = LoginProxy()

    def setup(self):
        time.sleep(3)



    # def teardown_class(self):
    #     time.sleep(3)
    #     DriverUtil.get_mp_quit()





    # 登录成功
    @pytest.mark.parametrize("mobile, code, username", build_data())
    def test_login(self, mobile, code, username):
        logging.info("mobile, code, username"+mobile + code+ username)

        # 登录
        self.login_proxy.click_login(mobile, code)

        # 断言
        is_exist = utils.exist_text(DriverUtil.get_mp_driver(), username)
        assert is_exist
