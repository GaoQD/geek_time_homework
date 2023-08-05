"""
============================
@description:TODO
@author:gaoqd
@time:2023/7/16  20:58
@version: 1.0
@file: wework_page.py
============================
"""
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class WeworkPage(BasePage):

    def __init__(self, driver=None, caps=None):
        caps = {}
        # 保留登录状态 noReset = True
        caps['noReset'] = True
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = 'com.tencent.wework.launch.LaunchSplashActivity'
        super().__init__(driver, caps)
        self.driver.implicitly_wait(5)

    def address_book(self) -> ListPage:
        self.click(By.XPATH, "//*[@text='通讯录']")
        return ListPage(self.driver)

    def staging(self):
        self.click(By.XPATH, "//*[@text='工作台']")

