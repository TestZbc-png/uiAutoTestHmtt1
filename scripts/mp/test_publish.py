import time
import pytest
import utils
from page.mp.home_page import  HomeProxy
from page.mp.publish_page import PublishProxy
import logging


@pytest.mark.run(order=3)
class TestPublish:

    def setup_class(self):
        self.driver = utils.DriverUtil.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()

    def setup(self):
        time.sleep(3)



    def teardown(self):
        utils.DriverUtil.get_mp_driver().get("http://ttmp.research.itcast.cn/#/login")
        time.sleep(3)

    def test_click_to_home_list(self):
        # 测试数据
        title = "zbcceshi001"
        content = "吴迪阿三接电话"
        channel = "数据库"

        # 跳转文章发布页
        self.home_proxy.to_article_page()

        # 发布文章
        self.publish_proxy.publish_article(title, content, channel)
        logging.info("title={}, content={}, channel={}".format(title, content, channel))
        # 断言
        is_exist = utils.exist_text(self.driver, "新增文章成功")
        assert is_exist