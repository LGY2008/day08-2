from base.base import Base
import page


class PageOrder(Base):
    # 点击 我的购物车
    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)

    # 点击 去结算
    def page_click_account(self):
        self.base_click(page.order_account)

    # 定位收货人
    def page_find_person(self):
        self.base_find(page.order_person)

    # 提交订单
    def page_submit_order(self):
        self.base_click(page.order_submit)

    # 获取订单提交结果
    def page_get_submit_resut(self):
        return self.base_get_text(page.order_result)

