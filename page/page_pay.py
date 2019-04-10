from base.base import Base
import page


class PagePay(Base):
    # 点击我的订单
    def page_click_my_order_link(self):
        self.base_click(page.pay_my_order)

    # 点击 立即支付
    def page_click_now_pay(self):
        # 切换 窗口
        self.base_click(page.pay_now_pay)

    #
