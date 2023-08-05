
"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/5  18:08
@version: 1.0
@file: admin_page.py
============================
"""
from __future__ import annotations
from framework.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from wework.contract.list_page import ListPage


class AdminPage(BasePage):
    # 定位【添加成员】
    _add_member = dict(by=AppiumBy.ID, value='com.tencent.wework:id/g18')
    # 定位【手动输入添加】
    _manual = dict(by=AppiumBy.XPATH, value='//*[@text="手动输入添加"]')
    # 输入姓名
    _input_username = dict(by=AppiumBy.ID, value='com.tencent.wework:id/c1a')
    # 输入手机号
    _input_phone = dict(by=AppiumBy.ID, value='com.tencent.wework:id/iaq')
    # 保存
    _save = dict(by=AppiumBy.ID, value='com.tencent.wework:id/b0b')
    # 返回
    _back = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lea')
    # 右上角“x” ，取消
    _cancel = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lf0')

    def add_member(self, name, phone) -> AdminPage:
        self.click(**self._add_member)
        self.click(**self._manual)
        self.send_keys(**self._input_username, text=name)
        self.send_keys(**self._input_phone, text=phone)
        self.click(**self._save)
        # 隐式等待
        self.driver.find_element(**self._manual)
        self.click(**self._back)

        return self

    def add_branch(self, name) -> AdminPage:
        ...

    def edit_branch_name(self, name) -> AdminPage:
        ...

    def cancel(self) -> ListPage:
        self.click(**self._cancel)
        return ListPage(self.driver)
