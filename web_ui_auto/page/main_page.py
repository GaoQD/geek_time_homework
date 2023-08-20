"""
============================
@description:TODO
@author:gaoqd
@time:2023/8/6  16:33
@version: 1.0
@file: main_page.py
============================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.base_page import BasePage
from page.search_page import SearchPage
from utils.data_reader import DataReader
from utils.path import data_path

cookies_path = os.path.join(data_path, 'ceshiren_cookies.json')
cookies = DataReader.load_json(cookies_path)


class MainPage(BasePage):
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            super().__init__(driver)
            self.driver.get("https://ceshiren.com/")
            self.screen_shot()
        self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.screen_shot()

    def get_topic_list(self) -> list[dict]:
        ...

    def to_search_advance(self) -> SearchPage:
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "current_user")))
        self.click(By.CSS_SELECTOR, '#search-button[title="搜索"]')
        # 高级搜索
        self.click(By.CSS_SELECTOR, '.show-advanced-search')
        return SearchPage(self.driver)

    def close(self):
        self.close()
