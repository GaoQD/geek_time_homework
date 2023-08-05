"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/5  18:20
@version: 1.0
@file: profile_page.py
============================
"""
from framework.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

class ProfilePage(BasePage):
    _name = dict(by=AppiumBy.ID, value='com.tencent.wework:id/kps')
    _mail = dict(by=AppiumBy.ID, value='com.tencent.wework:id/c22')
    _depart = dict(by=AppiumBy.ID, value='com.tencent.wework:id/cad')
    _back = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lea')

    # 操作更多
    _more = dict(by=AppiumBy.ID, value='com.tencent.wework:id/lf0')
    # 编辑成员
    _edit = dict(by=AppiumBy.ID, value='com.tencent.wework:id/c8r')
    # 删除1
    _delete1 = dict(by=AppiumBy.ID, value='com.tencent.wework:id/gvm')
    # 删除2
    _delete2 = dict(by=AppiumBy.ID, value='com.tencent.wework:id/cw1')

    def get_info(self) -> dict:
        name = self.driver.find_element(**self._name).text
        mail = self.driver.find_element(**self._mail).text
        depart = self.driver.find_element(**self._depart).text
        self.click(**self._back)
        self.click(**self._back)
        # print(name, mail, depart)
        return dict(name=name, mail=mail, depart=depart)

    def delete(self):
        self.click(**self._more)
        self.click(**self._edit)

        # 滑动屏幕
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        start_x = width / 2
        start_y = height - 100
        end_x = width / 2
        end_y = 100
        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()
        self.driver.implicitly_wait(5)

        self.click(**self._delete1)
        self.click(**self._delete2)
        self.click(**self._back)
