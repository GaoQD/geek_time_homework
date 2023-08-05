"""
============================
@description:TODO
@author:gaoqd
@time:2023/7/17  09:39
@version: 1.0
@file: list_page.py
============================
"""
from framework.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from wework.contract.admin_page import AdminPage
from wework.contract.profile_page import ProfilePage


class ListPage(BasePage):
    # 通讯录中的搜索按钮
    _search_button = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lf_')
    _item = dict(by=AppiumBy.ID, value='com.tencent.wework:id/f_k')
    _admin = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lf5')
    # _admin = dict(by=AppiumBy.ID, value='com.tencent.wework:id/l71')
    _input = dict(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')
    _back = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lea')

    def manage(self) -> 'AdminPage':
        self.click(**self._admin)
        return AdminPage(self.driver)

    def search(self, keyword) -> ProfilePage:
        self.click(**self._search_button)
        self.send_keys(**self._input, text=keyword)
        self.click(**self._item)
        return ProfilePage(self.driver)

    def scan(self, name) -> ProfilePage:
        ...
