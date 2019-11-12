import time

import pytest

import utils
from page.mis.article_audit_page import ArticleAuditProxy
from page.mis.home_page import HomeProxy

@pytest.mark.run(order=3)
class TestHome:

    def setup_class(self):
        self.proxy = HomeProxy()
        self.ariticle = ArticleAuditProxy()



    def test_article_audit(self):
        # 测试数据
        title = "ceshi001"
        status = "待审核"

        # 进入待审核页面
        self.proxy.click_to_audit_page()
        # 文章审核
        self.ariticle.click_to_article_audit(title, status)
        # 等待文章的审核
        time.sleep(2)
        # 断言
        is_exit = self.ariticle.is_pass_audit(title)
        assert is_exit


