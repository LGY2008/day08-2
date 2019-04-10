import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        PageLogin(self.driver).page_login_success()
        self.order = PageOrder(self.driver)
        self.order.base_index()

    def tearDown(self):
        sleep(2)
        GetDriver().quit_driver()

    def test_order(self):
        # 点击 我的购物车
        self.order.page_click_my_cart()
        # 点击 去结算
        self.order.page_click_account()
        # 定位收货人
        self.order.page_find_person()
        # 提交订单
        self.order.page_submit_order()
        # 获取订单结果
        msg = self.order.page_get_submit_resut()
        print("msg:", msg)