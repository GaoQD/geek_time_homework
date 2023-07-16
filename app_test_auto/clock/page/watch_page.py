from __future__ import annotations
from appium.webdriver.common.appiumby import AppiumBy
from clock.page.base_page import BasePage


class WatchPage(BasePage):

    def start(self) -> WatchPage:
        self.click(AppiumBy.ACCESSIBILITY_ID, "Start")
        return self

    def pause(self) -> WatchPage:
        self.click(AppiumBy.ACCESSIBILITY_ID, "Pause")
        return self

    def reset(self) -> WatchPage:
        self.click(AppiumBy.ACCESSIBILITY_ID, "Reset")
        return self

    def lap(self) -> WatchPage:
        self.click(AppiumBy.ACCESSIBILITY_ID, "Lap")
        return self

    def share(self) -> WatchPage:
        ...

    def get_total_time(self) -> float:
        return float(
            self.find(AppiumBy.ID, 'com.google.android.deskclock:id/stopwatch_time_text').text + '.' + self.find(
                AppiumBy.ID, 'com.google.android.deskclock:id/stopwatch_hundredths_text').text)

    def get_lap_list(self) -> list[dict]:
        lap_list = []
        for element in self.driver.find_elements(AppiumBy.ID, 'com.google.android.deskclock:id/lap_number'):
            lap_list.append(element.text)
        return lap_list
