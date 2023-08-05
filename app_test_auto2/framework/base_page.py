"""
============================
@description:TODO
@author:gaoqd
@time:2023/7/17  09:10
@version: 1.0
@file: base_page.py
============================
"""
import allure
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver=None, caps=None):
        if driver is not None:
            self.driver: WebDriver = driver
        else:
            if caps is None:
                caps = {}
            caps["platformName"] = "android"
            # 当界面不停变化的时候，不要等界面处于空闲状态
            caps['settings[waitForIdleTimeout]'] = 0
            caps["appium:ensureWebviewsHavePages"] = True
            caps["appium:nativeWebScreenshot"] = True
            caps["appium:newCommandTimeout"] = 3600
            caps["appium:connectHardwareKeyboard"] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.driver.find_element(by, value).click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def send_keys(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
