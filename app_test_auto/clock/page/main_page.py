from __future__ import annotations
from appium.webdriver.common.appiumby import AppiumBy
from clock.page.base_page import BasePage
from clock.page.watch_page import WatchPage


class MainPage(BasePage):

    def __init__(self, driver=None):
        # app入口
        caps = {}
        caps['appPackage'] = 'com.google.android.deskclock'
        caps['appActivity'] = "com.android.deskclock.DeskClock"
        super().__init__(driver, caps)

    def add_city(self, city_name) -> MainPage:
        self.click(AppiumBy.ACCESSIBILITY_ID, "Cities")
        self.send_keys(AppiumBy.ID, "com.google.android.deskclock:id/search_src_text", text=city_name)
        self.click(AppiumBy.ID, "com.google.android.deskclock:id/city_name")
        return self

    def get_city_list(self) -> list[dict]:
        city_list = []
        for element in self.driver.find_elements(AppiumBy.ID, "com.google.android.deskclock:id/selectable_area"):
            name = element.find_element(AppiumBy.ID, 'com.google.android.deskclock:id/city_name').text
            time = int(
                element.find_element(AppiumBy.ID, 'com.google.android.deskclock:id/digital_clock').text.split(':')[0])
            city_list.append({
                'name': name,
                'time': time
            })
        return city_list

    def get_default_time(self) -> str:
        return int(
            self.driver.find_element(AppiumBy.ID, 'com.google.android.deskclock:id/digital_clock').text.split(':')[0])

    def to_watch(self) -> WatchPage:
        self.click(AppiumBy.XPATH, "//*[@text='Stopwatch']")
        return WatchPage(self.driver)
