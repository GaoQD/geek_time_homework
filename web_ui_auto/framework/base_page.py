"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/6  16:22
@version: 1.0
@file: base_page.py
============================
"""
import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Firefox()
        else:
            self.driver = driver

    def click(self, by, value):
        self.driver.find_element(by, value).click()
        self.screen_shot()

    def send_keys(self, content, by, value):
        self.driver.find_element(by, value).send_keys(content)
        self.screen_shot()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def screen_shot(self):
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def close(self):
        self.driver.quit()
